from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Intern
from .serializers import InternSerializer


# Create your views here.
@api_view(['GET'])
def urlOverview(request):
        endPoints = {
         "slackUsername": "enigma", 
         "backend": True, 
         "age": 28, 
         "bio": "Hi, I am Mirera aka enigma, interested in reverse engineering and web application security"
        }
        return JsonResponse(endPoints)

# @api_view(['GET'])
# def getInternsDetails(request,pk):
#         intern = Intern.objects.get(id=pk)
#         serializer = InternSerializer(intern, many=False)
#         return JsonResponse(serializer.data, safe=False)

