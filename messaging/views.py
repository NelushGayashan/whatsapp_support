import asyncio
from django.utils.timezone import now
from django.db import transaction
from asgiref.sync import sync_to_async, async_to_sync
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Message
from .serializers import MessageSerializer

@sync_to_async
def save_message(data):
    """
    Save message asynchronously in the database.
    """
    return Message.objects.create(
        sender=data["sender"],
        receiver=data["receiver"],
        content=data["content"],
        status="sent",
        timestamp=now()
    )

@api_view(["POST"])
def send_message(request):
    """
    DRF does not support async views directly. Use `async_to_sync` wrapper.
    """
    return async_to_sync(_send_message_async)(request)

async def _send_message_async(request):
    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
        message = await save_message(serializer.validated_data)
        return Response({"message": "Message sent asynchronously", "data": MessageSerializer(message).data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def webhook_handler(request):
    """
    Webhook to receive incoming WhatsApp messages (wrapped in `async_to_sync`).
    """
    return async_to_sync(_webhook_handler_async)(request)

async def _webhook_handler_async(request):
    data = request.data
    if "sender" in data and "content" in data:
        message = await save_message({
            "sender": data["sender"],
            "receiver": "Me",
            "content": data["content"],
        })
        return Response({"message": "Webhook received asynchronously", "data": MessageSerializer(message).data}, status=status.HTTP_200_OK)
    return Response({"error": "Invalid payload"}, status=status.HTTP_400_BAD_REQUEST)
