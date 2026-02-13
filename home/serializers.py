# serializers.py
from rest_framework import serializers
from .models import Murojaat

class MurojaatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Murojaat
        fields = "__all__"
        read_only_fields = ("id", "created_at")
