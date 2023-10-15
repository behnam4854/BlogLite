from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views.decorators.http import require_http_methods, require_safe
from django.views import View
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post
import datetime

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