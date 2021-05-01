from rest_framework import serializers

from .models import * 


class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker
        fields = ('id', 'name', 'speaker_type', 'num_speakers', 'max_watts', 'num_channels', 'price')

class SubwooferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subwoofer
        fields = ('id', 'name', 'subwoofer_type', 'rms_power', 'size', 'low_freq', 'high_freq', 'price')

class ReceiverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receiver
        fields = ('id', 'name', 'num_channels', 'rms_power', 'advanced_eq', 'price')

class ProjectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projector
        fields = ('id', 'name', 'brightness', 'aspect_ratio', 'resolution', 'price')

class ScreenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screen
        fields = ('id', 'name', 'height', 'width', 'screen_type', 'aspect_ratio', 'price')