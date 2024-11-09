from rest_framework import viewsets
from .models import Pais
from .serializer import PaisSerializers, verificar_duplicado
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

class LocalidadesTemplateView(TemplateView):
    template_name = "localidades/localidades.html"

# Vista para obtener la lista de países
class PaisListView(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializers
    permission_classes = [AllowAny]

    @action(detail=True, methods=['get'], url_path='codigo-telefonico-pais')
    def codigo_telefonico(self, request, pk=None):
        try:
            pais = self.get_object()
            return Response({'codigo_telefonico_pais': pais.codigo_telefonico_pais})
        except Pais.DoesNotExist:
            return Response({'error': 'País no encontrado'}, status=404)

# Vista de inicio
def home(request):
    return render(request, "home.html")

@api_view(['GET'])
def verificar_duplicado_api(request):
    campo = request.GET.get('campo')
    valor = request.GET.get('valor')
    modelo_str = request.GET.get('modelo')

    try:
        verificar_duplicado(modelo_str, campo, valor)
        return Response({"existe": False})
    except ValidationError as e:
        return Response({"existe": True, "mensaje":str(e)}, status=400)