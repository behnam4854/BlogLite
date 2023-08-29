from django.urls import path, include
from core.views import homeview,current_datetime, HomeClassBasedView

urlpatterns = [
        # path('', homeview, name='home'),
        path('', HomeClassBasedView.as_view(), name='home'),
        path('test/', current_datetime, name='test'),
    ]