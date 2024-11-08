from django.db import IntegrityError, transaction
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Pais
from .serializer import PaisSerializers
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView


class LocalidadesTemplateView(TemplateView):
    template_name = "localidades/localidades.html"


# Vista para obtener la lista de países
class PaisListView(APIView):
    def get(self, request):
        pais_id = request.query_params.get("pais_id")

        if pais_id:
            pais = get_object_or_404(Pais, id=pais_id)
            serializer = PaisSerializers(pais)
            return Response(serializer.data)
        else:
            paises = Pais.objects.all()
            serializer = PaisSerializers(paises, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = PaisSerializers(data=request.data)
        if serializer.is_valid():
            try:
                with transaction.atomic():
                    serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response(
                    {
                        "error": "El país ya existe o hay un problema de integridad de datos."
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            except Exception as e:
                return Response(
                    {"error": f"Error interno: {str(e)}"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Vista de inicio
def home(request):
    return render(request, "home.html")
