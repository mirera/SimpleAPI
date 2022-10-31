from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Intern
from .serializers import InternSerializer


# Create your views here.
@api_view(['GET'])
def getAllInterns(request):
        interns = Intern.objects.all()
        serializer = InternSerializer(interns, many=True)
        return JsonResponse(serializer.data, safe=False)
