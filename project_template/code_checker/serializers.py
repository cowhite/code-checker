from rest_framework import serializers

from .models import *


class CodeCompileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeCompile
        fields = (
            'source', 'language', 'test_cases', 'stderr', 'stdout', 'time',
            'is_correct')
        read_only_fields = ('stderr', 'stdout', 'is_correct', 'time')


