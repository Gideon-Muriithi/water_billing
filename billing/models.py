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
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user = id).first()
        return 

class Status (models.Model):
    Account_Meter_Number = models.BigIntegerField()
    Water_Connection = models.BooleanField(blank=True)
    Sewer_Connection = models.BooleanField(blank=True)
    Account_Category = models.TextField(max_length='30')
    Account_Status = models.TextField(max_length='20')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(f'Account_Meter_Number: {self.Account_Meter_Number}')


    @classmethod
    def get_account(cls, user):
        account = Status.objects.filter(user__pk = user)
        return account


class Payment(models.Model):
    Year = models.IntegerField()
    Month = models.TextField(max_length='12')
    C_F = models.IntegerField()
    Amount_Due = models.IntegerField()
    Amount_Paid = models.IntegerField()
    B_F = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(f'Latest Payment {self.Amount_Paid}')

    @classmethod
    def get_account(cls, user):
        account = Payment.objects.filter(user__pk = user)
        return account


class Bill(models.Model):
    year = models.IntegerField()
    month = models.TextField(max_length='30')
    previous_charges = models.IntegerField()
    current_charges = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount_due = models.IntegerField()

    def __str__(self):
        return str(f'Current_Bill{self.current_charges}')

    @classmethod
    def get_account(cls, user):
        account = Bill.objects.filter(user__pk = user)
        return account


class Unit(models.Model):
    year = models.IntegerField()
    month = models.TextField()
    previous_units = models.IntegerField()
    current_units = models.IntegerField()
    units_due = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(f'units_due: {self.units_due}')


    @classmethod
    def get_account(cls, user):
        account = Unit.objects.filter(user__pk = user)
        return account

class Detail(models.Model):
    account_number = models.IntegerField()
    account_name = models.TextField(max_length='20')
    phone_number = models.IntegerField()
    id_number = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.account_name)

    @classmethod
    def get_account(cls, user):
        account = Detail.objects.filter(user__pk = user)
        return account
