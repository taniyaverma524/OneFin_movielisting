from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from user.views import *

app_name = 'user'

urlpatterns = [
    path('gettoken/',jwt_views.TokenObtainPairView.as_view(),name ='token_obtain_pair'),
    path('register/',UserRegistrationApiView.as_view(),name='user_registeration'),
    path('login/',UserLoginAPIView.as_view(),name='login'),

]                                                                                                                                       