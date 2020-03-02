from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('accounts/',include('allauth.urls')),
    path('',TemplateView.as_view(template_name="login/index.html")),
]