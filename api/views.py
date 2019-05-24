from rest_framework.generics import ListAPIView
from api.models import News
from api.serializers import NewsSerializer


class RssList(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

