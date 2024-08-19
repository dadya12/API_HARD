from django.urls import path

from api_v1.views import echo, get_csrf_token

app_name = 'api_v1'

urlpatterns = [
    path('echo/', echo, name='echo'),
    path('get-token/', get_csrf_token, name='get_token'),

]
