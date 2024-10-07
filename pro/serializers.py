from rest_framework import serializers
from .models import outing,outpass,amiclean

#outpass
class outpassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = outpass
        fields=('name','plf','date','time')
#outing
class outingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = outing
        fields=('name','plf','date','time')
#amiclean
 
class amicleanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = amiclean
        fields=('name','plf','des','date','time')