from rest_framework import serializers
from .models import DocumentManagement;

class DocMgtSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentManagement
        fields = '__all__'