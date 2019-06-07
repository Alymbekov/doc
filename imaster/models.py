from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import IntegerRangeField

class User(AbstractUser):
    full_name= models.CharField(max_length=255)


    def __str__(self):
        return self.username

def upload_to(instance, filename):
    return 'profile_images/{0}/{1}'.format(instance.user.pk, filename)


class Company(models.Model):
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    default_profile_image = 'profile.jpg'
    logo = models.ImageField(
        default=default_profile_image,
        upload_to='static/images',
        null=True,
        blank=True
    )
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    ages = IntegerRangeField()
    start = models.DateTimeField()


    def __str__(self):
        return self.name



class Category(models.Model):
    title = models.CharField(max_length=255,)
    category = models.ForeignKey('self', related_name="categ", on_delete=models.CASCADE, null=True, blank=True)


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


    def __str__(self):
        return self.info



class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name="comments", on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)


    def approve(comment):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text



class Doctor(models.Model):
    doctor = models.ForeignKey('User', on_delete=models.CASCADE, related_name="doctors")
    default_profile_image = 'profile.jpg'
    photo = models.ImageField(
        default=default_profile_image,
        upload_to='static/images',
        null=True,
        blank=True
    )
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING, related_name="categories")
    post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name="doctors", null=True)
    company = models.ManyToManyField(Company)

    def __str__(self):
        return '%s' % self.doctor

    def get_absolute_url(self):
        return reverse('doctor-detail', kwargs={"pk": self.pk})
