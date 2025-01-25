from django.contrib import admin
from django.utils.html import format_html
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ("sender", "receiver", "content", "status", "timestamp", "send_message_button")  # Display relevant columns
    list_filter = ("status", "timestamp")  # Filter by message status and timestamp
    search_fields = ("sender", "receiver", "content")  # Search functionality for sender, receiver, and content

    def send_message_button(self, obj):
        # This button allows sending the message from the admin interface
        return format_html('<a class="button" href="{}">Send Message</a>', f"/api/send-message/?id={obj.id}")

    send_message_button.short_description = "Send Message"  # Short description for the button column

admin.site.register(Message, MessageAdmin)  # Register the Message model with custom admin configuration
