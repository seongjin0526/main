#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.db import connections

#REST-API
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import generics
from .serializers import SampleSerializer
from .serializers import LeadSerializer
from backend.models import Lead

#UTIL
import json

class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

def sample(request):

    """
    making logic
    """

    """
    with connections['default'].cursor() as cur:
        query = '''
            select *
            FROM table
            where sample = '{page}'
        '''.format(page=page)
        cur.execute(query)
        rows = cur.fetchall()
    """
    
    context = {}
    context['sample_key'] = 'hello world'

    return render(request, 'backend/sample.html', context)
    #return JsonResponse({'a':'b'})

class SampleView(CreateAPIView):

    serializer_class = SampleSerializer

    def create(self, request):
 
        id = request.POST.get('id')
        print("id = ", id)

        return Response({"result": "ok"})
