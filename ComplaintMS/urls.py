from django.urls import path
from . import views
from .views import reply_to_complaint,all_complaints_view,certificate
from django.contrib.auth import views as auth_views
from .views import check_user_registration

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('signin/', auth_views.LoginView.as_view(template_name='ComplaintMS/signin.html'), name='signin'),
    path('logout/', auth_views.LogoutView.as_view(template_name='ComplaintMS/logout.html'), name='logout'),
    path('password/', views.change_password, name='change_password'),
    path('passwords/', views.change_password_g, name='change_password_g'),
    path('counter/', views.counter, name='counter'),
    path('solved/', views.solved, name='solved'),
    path('reply/<int:complaint_id>/', reply_to_complaint, name='reply_to_complaint'),  # Corrected pattern
    path('login/', views.login, name='login'),
    path('list/', views.list, name='list'),
    path('pdf/', views.pdf_view, name='view'),
    path('pdf_g/', views.pdf_viewer, name='view'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('login_redirect/', views.login_redirect, name='login_redirect'),
    path('slist/', views.slist),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('complaints/', views.complaints, name='complaints'),
    path('allcomplaints/', views.allcomplaints, name='allcomplaints'),
    path('certificate/', views.certificate, name='certificate'),
path('api/check_user/', check_user_registration, name='check_user_registration'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='ComplaintMS/password_reset.html'), name='password_reset'),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(template_name='ComplaintMS/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='ComplaintMS/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='ComplaintMS/password_reset_complete.html'), name='password_reset_complete'),
]
