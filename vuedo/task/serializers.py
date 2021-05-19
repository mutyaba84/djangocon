from rest_framework import serializers

from .models import Variable


class VariableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Variable
        fields = ('id', 'name', 'type')
