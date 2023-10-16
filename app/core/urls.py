from django.urls import path, include
from core.views import PostlistView,PostDetailView
from rest_framework import routers
from .views import PostViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
        # path('', homeview, name='home'),
        # path('posts-old', PostlistView.as_view(), name='post-list'),
        # path("<slug:slug>/", PostDetailView.as_view(), name="post-detail"),
        path('', include(router.urls)),

        # path('test/', testView.as_view(greeting = 'Noooooooooooooo this is better'), name='test'),
    ]
