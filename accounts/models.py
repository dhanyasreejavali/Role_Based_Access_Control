from django.db import models
from django.contrib.auth.models import AbstractUser

# ✅ Custom user model
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    def __str__(self):
        return f"{self.username} ({self.role})"

# ✅ Team model
class Team(models.Model):
    name = models.CharField(max_length=100)
    manager = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='teams')

# ✅ Member model
class Member(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')
