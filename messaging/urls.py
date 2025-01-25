from django.urls import path
from .views import send_message, webhook_handler

urlpatterns = [
    path("api/send-message/", send_message, name="send_message"),
    path("api/webhook/", webhook_handler, name="webhook"),
]
