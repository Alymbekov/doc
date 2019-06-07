from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import IntegerRangeField

class User(AbstractUser):
    full_name= models.CharField(max_length=255)


    def __str__(self):
        return self.username

def upload_to(instance, filename):
    return 'profile_images/{0}/{1}'.format(instance.user.pk, filename)


class Company(models.Model):
    default_profile_image = 'profile.jpg'
    logo = models.ImageField(
        default=default_profile_image,
        upload_to=upload_to,
        null=True,
        blank=True
    )
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    ages = IntegerRangeField()
    start = models.DateTimeField()
    CHOICES =[
        ('ages', ages),
        ('start', start),
    ]
    time_of_work = models.CharField(choices=CHOICES, max_length=255)



class Category(models.Model):
    title = models.CharField(max_length=255,)
    category = models.ForeignKey('self', related_name="categ", on_delete=models.CASCADE, null=False, blank=True)


    def __str__(self):
        return self.title


class Post(models.Model):
    street_address = models.CharField(max_length=255)
    place_of_work = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    experience = models.PositiveIntegerField()
    info = models.TextField()
    education = models.TextField()
    treatment_of_diseases = models.TextField()
    shedule = models.TextField()



class Doctor(models.Model):
    doctor = models.ForeignKey('User', on_delete=models.CASCADE, related_name="doctors")
    default_profile_image = 'profile.jpg'
    photo = models.ImageField(
        default=default_profile_image,
        upload_to=upload_to,
        null=True,
        blank=True
    )
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING, related_name="categories")
    post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name="doctors", null=True)
    company = models.ManyToManyField(Company)

    def __str__(self):
        return self.doctor
