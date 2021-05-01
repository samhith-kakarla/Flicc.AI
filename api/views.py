from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import * 
from .models import * 


@api_view(['GET'])
def api_overview(request):

    return Response({
        "Flicc REST API URLs": {
            "Get Speakers": "/get-speakers", 
            "Get Subwoofer": "/get-subwoofer", 
            "Get AV Receiver": "/get-reciever", 
            "Get Projector": "/get-projector", 
            "Get Screen": "/get-screen", 
        }
    })

# INPUTS - Room Dimensions (Length, Width, Height)

@api_view(['POST'])
def get_speakers(request):
    room_length = request.length
    room_width = request.width 
    room_height = request.width 

    ideal = {}

    # Determine Ideal Type

    # Determine Ideal Sound Level

    # Pick and Return Best Speaker 
    return Response()


@api_view(['POST'])
def get_subwoofer(request):
    room_length = request.length
    room_width = request.width 
    room_height = request.height 

    ideal = {}

    # Determine Ideal Type

    # Determine Ideal Size

    # Determine Ideal RMS Power 

    # Pick and Return Best Subwoofer
    return Response()


@api_view(['POST'])
def get_receiver(request):
    room_length = request.length
    room_width = request.width 
    room_height = request.height 

    ideal = {}


@api_view(['POST'])
def get_projector(request):
    room_length = request.length
    room_width = request.width 
    room_height = request.height 

    ideal = {}


@api_view(['POST'])
def get_screen(request):
    room_length = request.length
    room_width = request.width 
    room_height = request.height 

    ideal = {}
    

