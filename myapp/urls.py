from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet
from . import drfview
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from myapp.versioning.v1 import ProfileViewV1
from myapp.versioning.v2 import ProfileViewV2


router = DefaultRouter()
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('hello/', views.hello),   # default route
    path('bye/', views.bye),   # default route
    path('echo/', views.echo),   # default route
    path('update/', views.update_echo),     # PUT
    path('delete/', views.delete_echo),     # DELETE
    path('cbv-post/', views.SimplePostView.as_view()),
    path('drf-post/', views.UserAPI.as_view()),
    path('', include(router.urls)),
    path('simple-products/', views.simple_page),
    path('newstudents/', views.student_api),
    path("login/", views.login_page),
    path("home/", views.home),
    path("defview/", drfview.ProfileAPI.as_view()),
    path("api-token-auth/", obtain_auth_token),
    path("jwt/login/", TokenObtainPairView.as_view()),
    path("jwt/refresh/", TokenRefreshView.as_view()),
    path('v1/profile/', ProfileViewV1.as_view(), name='profile-v1'),
    path('v2/profile/', ProfileViewV2.as_view(), name='profile-v2'),

]


