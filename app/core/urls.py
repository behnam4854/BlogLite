from django.urls import path, include
from core.views import PostlistView,PostDetailView

urlpatterns = [
        # path('', homeview, name='home'),
        path('', PostlistView.as_view(), name='post-list'),
        path("<slug:slug>/", PostDetailView.as_view(), name="post-detail"),

        # path('test/', testView.as_view(greeting = 'Noooooooooooooo this is better'), name='test'),
    ]