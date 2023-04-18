from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from account.models import Post
from .views import now
from rest_framework.views import APIView
from datetime import datetime
from rest_framework.response import Response
# Serializers define the API representation.

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= Post
        fields = ['title', 'sub_title']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = UserSerializer




class HealthCheck(APIView):

    def get(self, request=None, *args, **kwargs):
        data = {}
        if request.GET: data['query_params'] = request.GET
        if request.data: data['body'] = request.data
        data['message'] = 'Welcome to collateral release'
        data['current_time'] = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
        return Response(status=200, data=data)

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'post', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('', now, name='now'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

