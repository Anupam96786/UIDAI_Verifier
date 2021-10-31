from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import EKYC


def index(request):
    data={}
    data['apikey']='d058ce12-badd-448d-9727-81abab136e99'
    return render(request, "index.html",data)


def generate_qr(request):
    data={}
    data['apikey']='d058ce12-badd-448d-9727-81abab136e99'
    return render(request, "generate_qr.html",data)


@csrf_exempt
@api_view(["POST"])
def receive_xml(request):
    try:
        EKYC.objects.create(eKycXML=request.data["eKycXML"])
        return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
