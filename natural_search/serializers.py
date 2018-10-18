from natural_search.models import ProjetoList,Proposition, Proponent
from rest_framework import serializers


# Serializers define the API representation.
class ProjetoListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjetoList
        fields = '__all__'

# Serializers define the API representation.
class PropositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Proposition
        fields = '__all__'

# Serializers define the API representation.
class ProponentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Proponent
        fields = '__all__'