from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


def index(request):
    return render(request, "index.html")


def generate_qr(request):
    return render(request, "generate_qr.html")


@csrf_exempt
@api_view(["POST"])
def receive_xml(request):
    try:
        print(request.data["eKycXML"])
        return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)