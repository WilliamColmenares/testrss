from rest_framework.generics import ListAPIView
from api.models import News, ICE, Section, People
from api.serializers import NewsSerializer
from rest_framework import viewsets
from api.serializers import ICEListSerializer, ICECreateSerializer, PeopleSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import detail_route


class RssList(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class TrainViewSet(viewsets.ViewSet):
    # toto define a train serializer here
    def list(self, request):
        queryset = ICE.objects.all()
        serializer = ICEListSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ICECreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"Message": "There was an error"})
        serializer.save(
            name=request.data['name'],
            sections=[
                Section.objects.create(name="section_1"),
                Section.objects.create(name="section_2")
            ]
        )
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """retrieves a specific train by its pk"""
        queryset = ICE.objects.all()
        train = get_object_or_404(queryset, pk=pk)
        serializer = ICEListSerializer(train)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """updates the name of the train"""
        train = ICE.objects.get(id=pk)
        serializer = ICECreateSerializer(instance=train, data=request.data)
        if not serializer.is_valid():
            return Response({"Message": "There was an error"})
        serializer.save()
        return Response(serializer.data)

    @detail_route(methods=['get', 'post'], url_path='persons')
    # Added get method to show it in the browsable api
    def persons(self, request, pk):
        """returns a list of persons which are curently on a specific train"""
        train_obj = ICE.objects.get(id=pk)
        sections_ids = train_obj.sections.values_list(flat=True)
        qs = People.objects.none()
        for elem in sections_ids:
            qs = qs.union(People.objects.filter(section=elem))
        serializer = PeopleSerializer(qs, many=True)
        return Response(serializer.data)
