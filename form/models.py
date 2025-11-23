from django.db import models
from service.models import Jobs  # Import the Jobs model

class userForm(models.Model):
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE, blank=True, null=True, related_name='applications')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # ✅ Add this line

    def __str__(self):
        return f"{self.name} - {self.job}"