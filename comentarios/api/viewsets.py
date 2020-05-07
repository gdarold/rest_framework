from rest_framework.viewsets import ModelViewSet

from comentarios.api.serializers import ComentarioSerializer
from comentarios.models import Comentarios


class ComentarioViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Comentarios.objects.all()
    serializer_class = ComentarioSerializer
