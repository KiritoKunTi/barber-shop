from django.db import models
from django.urls import reverse

# Create your models here.
class FAQ(models.Model):
    question = models.CharField('Question', max_length=100, default='Question: ')
    answer = models.TextField('Answer', default='Manager will give the answer...')
    
    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name_plural = 'FAQ'
        
    
    
class Comments(models.Model):
    client_name = models.CharField('Name', max_length=50)
    comment = models.TextField('Comment')
    
    def __str__(self):
        return self.client_name
    
    class Meta:
        verbose_name_plural = 'Comments'
    
    
    
class Services(models.Model):
    service_name = models.CharField('Service name', max_length=50)
    service_cost = models.CharField('Service cost', max_length=20)
    about = models.TextField('About service')    
    
    def __str__(self):
        return self.service_name
    
    class Meta:
        verbose_name_plural = 'Services'

    
class Barbers(models.Model):
    barber_name = models.CharField('Name', max_length=50)
    work_name = models.CharField('Work name', max_length=30)
    about_barber = models.TextField('About barber')
    barber_photo = models.ImageField('Photo')
    
    def __str__(self):
        return self.barber_name
    
    class Meta:
        verbose_name_plural = 'Barbers'
        
        
class Resumes(models.Model):
    first_name = models.CharField('First Name', max_length=20)
    last_name = models.CharField('Last Name', max_length=20)
    email = models.EmailField('Email')
    phone = models.CharField('Phone', max_length=16)
    summary = models.TextField('Message')
    picture = models.ImageField('Upload Files')
    
    def __str__(self):
        return self.last_name
    
    class Meta:
        verbose_name_plural = 'Resumes'
    
    
    
    
    
    
    
    
    