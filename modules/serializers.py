from rest_framework import serializers
from modules.models import Module
from modules.validators import TitleValidator


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'
        validators = [TitleValidator(field='title')]
