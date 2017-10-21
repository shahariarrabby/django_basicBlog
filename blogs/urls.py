from django.conf.urls import url
from blogs import views


urlpatterns = [
    url(r'^about/$', views.AboutView.as_view(),name='about'),

]
