from django.db import models

class Message(models.Model):
    sender = models.CharField(max_length=20)
    receiver = models.CharField(max_length=20)
    content = models.TextField()
    status = models.CharField(
        max_length=10,
        choices=[("sent", "Sent"), ("failed", "Failed")],
        default="sent"
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender} to {self.receiver}"
