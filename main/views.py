from rest_framework import viewsets, generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Topic, Comment
from .serializers import TopicSerializer, TopicFlatSerializer, CommentSerializer

class TopicFlatViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicFlatSerializer

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class HTMLAPIView(viewsets.ViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'
    serializer_class = TopicSerializer

    def list(self, request):
        queryset = Topic.objects.all()        
        return Response({'queryset': queryset}) 