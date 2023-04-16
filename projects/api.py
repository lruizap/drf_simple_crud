from projects.models import Project
from rest_framework import viewsets, permissions
from projects.serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):

    # Consulta todos los datos de la tabla
    queryset = Project.objects.all()

    # Establecemos los permisos
    permission_classes = [permissions.AllowAny]

    # Aquí vamos a indicar a partir de que serializer va a
    # convertir los datos
    serializer_class = ProjectSerializer