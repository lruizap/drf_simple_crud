from rest_framework import serializers
from .models import Project

# Esta clase lo que hará será transformar un modelo en datos
# que van a poder ser consultados


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'id',
            'title',
            'description',
            'technology',
            'created_at'
        )
        read_only_fields = ('created_at', )
