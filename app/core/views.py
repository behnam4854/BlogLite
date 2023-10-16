from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods, require_safe
from django.views import View
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from requests import Response
from .models import Post
import datetime
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, PostSerializer


class PostlistView(ListView):
    """for retriving all the post in the home view"""
    model = Post
    # paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = datetime.datetime.now()
        return context

class PostDetailView(DetailView):
    """for views the single post detail view and reviewing it"""
    model = Post

class UserViewSet(viewsets.ModelViewSet):
    """view for managing the user"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated,]

    # def list(self, request):
    #     queryset = User.objects.all()
    #     serializer = UserSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     queryset = User.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = UserSerializer(user)
    #     return Response(serializer.data)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAdminUser,]


# @require_safe
# def homeview(request):
#     """the first version of home view using simple functions"""
#     # return HttpResponse("<h1>Page was found</h1>")
#     return render(request,'base.html')
# async def current_datetime(request):
#     now = datetime.datetime.now()
#     html = "<html><bo`dy>It is now %s.</body></html>" % now
#     return HttpResponse(html)
# class HomeClassBasedView(View):
#     """this is for home view using generic class based view"""
#     def get(self, request):
#         now = datetime.datetime.now()
#         html = "<html><body>It is now %s.</body></html>" % now
#         return HttpResponse(html)
# class testView(View):
#     greeting = "hi how are you"

#     def get(self, request):
#         return HttpResponse(self.greeting)
