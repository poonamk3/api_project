# from django.shortcuts import render
# from django.http import httprequest
# from django.http import httpResponse

# # Create your views here.
# def my_views(request):
# 	return httprequest("hello")

from django.http import HttpResponse
import datetime

def now(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = UserSerializer