from rest_framework import viewsets
from .models import outpass,outing,amiclean
from  .serializers import outingSerializer,outpassSerializer,amicleanSerializer



class outpassViewSet(viewsets.ModelViewSet):
    queryset=outpass.objects.all()
    serializer_class=outpassSerializer

class outingViewSet(viewsets.ModelViewSet):
    queryset=outing.objects.all()
    serializer_class=outingSerializer

class amicleanViewSet(viewsets.ModelViewSet):
    queryset=amiclean.objects.all()
    serializer_class=amicleanSerializer