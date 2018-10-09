from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from main import views as main_api


router = routers.DefaultRouter()
router.register(r'topic', main_api.TopicViewSet)
router.register(r'topic-flat', main_api.TopicFlatViewSet)
router.register(r'comment', main_api.CommentViewSet)


urlpatterns = [
    url(r'^docs/', include_docs_urls(title='My API')),
    url(r'^', include(router.urls)),
    url(r'^html/', main_api.HTMLAPIView.as_view({'get': 'list'}), name='html')
]
