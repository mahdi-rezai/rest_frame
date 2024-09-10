from django.urls import path
from . import views
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView



app_name = 'accounts'

urlpatterns=[
    path('register/',views.UserRegister.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('mahdi/',views.UserApi.as_view()),
]



router = routers.SimpleRouter()
router.register('user',views.UserViewSet)
urlpatterns +=router.urls


# {
# 	"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTc5MTkwNiwiaWF0IjoxNzI1NzA1NTA2LCJqdGkiOiI4NTM0YjAwODY5MjU0Yzk0OWQ0OWU1OGUwYmUxYzRhMiIsInVzZXJfaWQiOjh9.NOFpC7gIjrFP9mZ1nVhyg-o1NH0TvEKIGfulD18hWv0",
# 	"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI1NzA1ODA2LCJpYXQiOjE3MjU3MDU1MDYsImp0aSI6IjAyNTExMzZhNWEzMDRjN2ViM2I2NzI3ZTFmNGU3ZDI1IiwidXNlcl9pZCI6OH0.Ys6o72PEJvjWPFm6iwTKSHiOKtwhRFaLwrC2d829koQ"
# }