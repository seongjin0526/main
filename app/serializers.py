from rest_framework import serializers
from app.models import Lead

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ('id', 'name', 'email', 'message')
        #fields = '__all__'

class SampleSerializer(serializers.Serializer):

    id = serializers.CharField()

