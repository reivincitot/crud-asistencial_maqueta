from rest_framework import viewsets
from .models import Pais
from .serializer import PaisSerializers
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response




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
