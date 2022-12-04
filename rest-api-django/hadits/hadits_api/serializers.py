from rest_framework import serializers
from .models import ShahihBukharis

class ShahihBukharisSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShahihBukharis
        fields = ["kitab", "terjemah", "arab"]