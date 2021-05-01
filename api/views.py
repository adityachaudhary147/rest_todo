from django.shortcuts import render
# from django import httprespin
from django.http import HttpResponse, HttpResponseNotFound
from api.models import Task
from rest_framework.decorators import api_view
# Create your views here.
from api.serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework import status

def sample(request):
    return HttpResponse('<h1>Page was found</h1>')
@api_view(['GET'])
def TaskList(request):
    if request.method =='GET':
        tasks=Task.objects.all()
        serializer=TaskSerializer(tasks,many=True)
        print("el")
        return Response(serializer.data)

@api_view(['GET'])
def Task_ind(request,pk):
    if request.method=='GET':
        try:
            task=Task.objects.get(id=pk)
        except Task.DoesNotExist:
            return HttpResponse(status=404)
        serializer=TaskSerializer(task,many=False)
        return Response(serializer.data)

@api_view(['POST'])
def Task_fit(request):
    if request.method=='POST':
        data = {'desc': request.data.get('desc'), 'status': request.data.get('status')}
        serializer=TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

