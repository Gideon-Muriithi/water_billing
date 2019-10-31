from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    profile_photo = models.ImageField(default='default.jpg', upload_to='profile_pics/')
    bio = models.TextField(blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(user = id)
        return profile

class Status (models.Model):
    Account_Meter_Number = models.BigIntegerField()
    Water_Connection = models.BooleanField(blank=True)
    Sewer_Connection = models.BooleanField(blank=True)
    Account_Category = models.TextField(max_length='30')
    Account_Status = models.TextField(max_length='20')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return str(f'Account_Meter_Number: {self.Account_Meter_Number}')


    @classmethod
    def get_account(cls, user):
        account = Status.objects.filter(user__pk = user)
        return account