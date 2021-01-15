from .models import MainModel
from .serializers import MainModelSerializer
from rest_framework import viewsets

class MainModelViewSet(viewsets.ModelViewSet):
	serializer_class = MainModelSerializer
	queryset = MainModel.objects.all()
