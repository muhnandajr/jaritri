from django.conf.urls import url, include
from rest_framework import routers
from authentication.views import UserViewSet
from django.contrib.auth import views as auth_views

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
    url('change-password/', auth_views.PasswordChangeView.as_view()),
    # url('change-password/', auth_views.PasswordChangeDoneView.as_view()),
    # url('reset-password/', auth_views.PasswordResetView.as_view()),
    # url('reset-password/', auth_views.PasswordResetDoneView.as_view()),
    # url('password_reset_confirm/', auth_views.PasswordResetConfirmView.as_view()),
    # url('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view()),
]