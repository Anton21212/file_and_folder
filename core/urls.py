from django.urls import path

from core.views import MetaView

urlpatterns = [
    path('meta/', MetaView.as_view())
]
