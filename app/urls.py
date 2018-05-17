from django.urls import path
from django.conf.urls import url
from . import views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='happy API')

urlpatterns = [
    # rest-api
    url('api_sample$', views.SampleView.as_view()),

    # rest-swagger
    url('swagger$', schema_view),

    # main-url
    url('sample$', views.sample, name='sample'),
    url('api/lead$', views.LeadListCreate.as_view()),
]
