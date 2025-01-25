import asyncio
from .models import Message
import logging

logger = logging.getLogger(__name__)

async def send_message(sender, receiver, content):
    try:
        # Simulate sending a message asynchronously
        message = await asyncio.to_thread(
            Message.objects.create, sender=sender, receiver=receiver, content=content, status='sent'
        )
        logger.info(f"Message sent: {message}")
        return message
    except Exception as e:
        logger.error(f"Failed to send message: {e}")
        raise

async def process_webhook(data):
    try:
        sender = data.get('sender')
        receiver = data.get('receiver')
        content = data.get('content')

        # Handle missing fields or invalid data here if necessary
        if not sender or not receiver or not content:
            raise ValueError("Missing required fields in webhook data")

        # Simulate async database operation
        await asyncio.to_thread(
            Message.objects.create, sender=sender, receiver=receiver, content=content, status='received'
        )
    except Exception as e:
        logger.error(f"Failed to process webhook data: {e}")
        raise
