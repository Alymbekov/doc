from django.urls import path
from .views import (
    index, about, appointment,
    blogsingle, blog, contact,
    department,pricing,
    DoctorViewList, DoctorDetailView,
    )


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name="about"),
    path('appointment/', appointment, name="appointment"),
    path('blogsingle/', blogsingle, name="blogsingle"),
    path('blog/', blog, name="blog"),
    path('contact/', contact, name="contact"),
    path('department/', department, name="department"),
    path('doctor/', DoctorViewList.as_view(), name="doctor"),
    path('doctor/<int:pk>/',DoctorDetailView.as_view(), name="doctor-detail"),
    path('pricing/', pricing, name="pricing"),
]
