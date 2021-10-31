from django.urls import path
from django.conf.urls import include,url
from . import views
from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    path('', views.index,name='index'),
    path('sw.js', TemplateView.as_view(template_name='sw.js', content_type='application/x-javascript')),
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
]
