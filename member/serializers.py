from .models import Member #import member model
from django.contrib.auth.models import User # import user model
from rest_framework import serializers


# Create member serializer
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'