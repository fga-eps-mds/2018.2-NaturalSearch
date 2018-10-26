from natural_search.models import Project, Proponent
from rest_framework import serializers


# Serializers define the API representation.
class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

# Serializers define the API representation.
class ProponentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Proponent
        fields = '__all__'