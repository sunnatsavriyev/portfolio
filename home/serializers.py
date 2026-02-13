# serializers.py
from rest_framework import serializers
from .models import Murojaat

class MurojaatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Murojaat
        fields = "__all__"
        read_only_fields = ("id", "created_at")

    
    def validate(self, data):
        missing_fields = []
        for field in ["firstname", "lastname", "email", "murojaat"]:
            if not data.get(field):
                missing_fields.append(field)

        if missing_fields:
            raise serializers.ValidationError(
                {field: "Iltimos, bu maydonni to'ldiring." for field in missing_fields}
            )
        return data