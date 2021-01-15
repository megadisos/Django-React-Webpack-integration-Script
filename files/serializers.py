from rest_framework import serializers
from .models import MainModel

class MainModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = MainModel
		fields = ['id','name','description']

       