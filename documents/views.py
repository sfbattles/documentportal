from django.shortcuts import render
from rest_framework import viewsets
from .models import DocumentManagement
from .serializers import DocMgtSerializer

class DocumentAllView(viewsets.ModelViewSet):
    queryset = DocumentManagement.objects.all()
    serializer_class = DocMgtSerializer