from asyncore import read
from sys import platform
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
# Create your models here.

class User(models.Model):
    CID = models.IntegerField(primary_key=True)
    user  = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    gen = [
        ('Male', 'Male'),
        ('Female', 'Female')
        ]
    gender = models.CharField(max_length=100, choices = gen)
    DOB = models.DateField()
    profile = models.ImageField(upload_to='image', null= True, default=None, blank=True)
    Village = models.CharField(max_length=100)
    Chiwog = models.CharField(max_length=100)
    ThramNo = models.CharField(max_length=100)
    HouseHoldNo = models.CharField(max_length=100)  
    Created = models.DateTimeField(auto_now_add=True)
    contact_number = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    status = models.BooleanField(default=False)


    def __str__(self):
        return str(self.CID)

 
class Marriage(models.Model):
    MarriageID = models.CharField(max_length=100)
    YOUR_CId = models.OneToOneField(User, related_name="Your_CID", on_delete=models.CASCADE)
    Spouce_ID = models.OneToOneField(User, related_name="Spouce", on_delete=models.CASCADE)
    # YOUR_CId = models.ForeignKey(MaleUserData, related_name="Your_CID", on_delete=models.CASCADE)
    # Spouce_ID = models.ForeignKey(FemaleUserData, related_name="Spouce", on_delete=models.CASCADE)
    # Marriage_certificate = models.ImageField(upload_to='image')
    # Marriage_certificate1 = models.ImageField(upload_to='image')
    Marriage_certificate = models.ImageField(upload_to='image', null = True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.YOUR_CId.Name + " & " + self.Spouce_ID.Name

class ChildData(models.Model):
    Child_name = models.CharField(max_length=255)
    DOB_child = models.DateField()
    Marriage_ID = models.ForeignKey(Marriage, related_name="parents_Marriage_ID", on_delete=models.CASCADE)
    birth_certificate = models.ImageField(blank=True, upload_to = "birth_certificate")
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.Child_name





















# class Watchlist(models.Model):
#     title = models.CharField(max_length=100)
#     storyline = models.CharField(max_length=200)
#     platform = models.ForeignKey(StreamPlatforms, on_delete=models.CASCADE, related_name='watchlist')
#     active = models.BooleanField(default=True)
#     avg_rating = models.FloatField(default=0)
#     no_of_rating = models.IntegerField(default=0)
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title

# class Review(models.Model):
#     review_user = models.ForeignKey(User, on_delete=models.CASCADE)
#     rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
#     description = models.CharField(max_length=255)
#     Watchlist = models.ForeignKey(Watchlist, on_delete=models.CASCADE, related_name="reviews")
#     active = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return str(self.rating) + " |  " + self.Watchlist.title + " | " + str(self.review_user)


# class UserData(models.Model):
#     g = [
#         ('Male', 'Male'),
#         ('Female', 'Female')
#         ]
#     CID = models.IntegerField(unique=True)
#     Name = models.CharField(max_length=150)
#     DOB = models.DateField()
#     Gender = models.CharField(max_length=20,choices= g)
#     profile = models.ImageField(upload_to='image', null= True, default=None, blank=True)
#     # Gender = models.CharField(max_length=20, default='Male')
#     Village = models.CharField(max_length=100)
#     Chiwog = models.CharField(max_length=100)
#     ThramNo = models.CharField(max_length=100)
#     HouseHoldNo = models.CharField(max_length=100)  
#     Created = models.DateTimeField(auto_now_add=True)
#     contact_number = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100, unique=True)
#     status = models.BooleanField(default=False)

#     def __str__(self):
#         return self.Name