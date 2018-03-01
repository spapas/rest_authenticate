from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import HomeTemplateView, TestAuthView, LogoutViewEx
from rest_auth.views import LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('test_auth/', TestAuthView.as_view(), name='test_auth', ),
    path('rest-auth/logout/', LogoutViewEx.as_view(), name='rest_logout', ),
    path('rest-auth/login/', LoginView.as_view(), name='rest_login', ),
    path('', HomeTemplateView.as_view(), name='home', ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
