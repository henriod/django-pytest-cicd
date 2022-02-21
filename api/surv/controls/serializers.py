from rest_framework import serializers
from controls.models import Control


class ControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Control
        fields = "__all__"
