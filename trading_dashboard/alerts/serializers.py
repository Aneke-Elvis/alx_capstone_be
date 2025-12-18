from rest_framework import serializers
from .models import Alert

class AlertSerializer(serializers.ModelSerializer):
    class meta:
        models = Alert
        fields = '__all__'