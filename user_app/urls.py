from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from .views import registration_view
from .views import logout_view
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    #for token authentication
    path('login/', obtain_auth_token, name='login'),
    path('register/', registration_view, name='register'),
    path('logout/',logout_view, name='logout'),
    
    #for jwt authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #access token valid for 5 minutes
    # refresh tokenvalid for 24 hours
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    ]