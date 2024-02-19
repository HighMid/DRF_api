# serializers.py
from rest_framework import serializers
from .models import SomeItem

class SomeItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SomeItem
        fields = ['id', 'owner', 'name', 'description', 'rarity', 'created_at', 'updated_at']
