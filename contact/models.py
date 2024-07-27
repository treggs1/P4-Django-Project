from django.db import models
  
class Contact(models.Model):
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    new_message = models.BooleanField()
    
    def __str__(self):
        return self.email
