from django.urls import path
from . import views

urlpatterns = [
    path('', views.entry, name='entry'),
    path('signup/', views.signup_view, name='signup'),
    path('onboarding/verify/', views.verify_otp_view, name='verify_otp'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('translator/', views.translator, name='translator'),
    path('upload/', views.upload_pdf_view, name='upload_pdf'),
    path('chat/session/<uuid:session_id>/', views.chat_session_view, name='chat_session'),
    path('predict/', views.predict_appeal_view, name='predict_appeal'),
    path('documents/', views.document_list_view, name='document_list'),
    path('documents/<int:document_id>/', views.document_detail_view, name='document_detail'),
    path('chat/<uuid:session_id>/attach/', views.attach_document_view, name='attach_document'),
    path('about/', views.about, name='about'),
    path('forgot-password/', views.forgot_password_view, name='forgot_password'),
    path('reset-password-otp/', views.reset_password_otp_view, name='reset_password_otp'),
    path('reset-password/', views.reset_password_view, name='reset_password'),
    path('delete-chat/<uuid:session_id>/', views.delete_chat_session_view, name='delete_chat_session'),
    path('upload-profile-pic/', views.upload_profile_pic, name='upload_profile_pic'),
]
