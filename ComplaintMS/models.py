from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

from django.core.validators import RegexValidator
from datetime import datetime

class Meta:

    app_label = 'GEyan'
class Profile(models.Model):
    typeuser =(('student','student'),('grievance', 'grievance'))
    COL=(('Woodbridge School','Woodbridge School'),('Long View Public School','Long View Public School')) #change college names
    user =models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    School=models.CharField(max_length=29,choices=COL,blank=False)
    phone_regex =RegexValidator(regex=r'^\d{10,10}$', message="Phone number must be entered in the format:Up to 10 digits allowed.")
    contactnumber = models.CharField(validators=[phone_regex], max_length=10, blank=True)
    type_user=models.CharField(max_length=20,default='student',choices=typeuser)
    CB=(('IX',"IX"),('X',"X"),('XI',"XI"),('XII',"XII"))
    Branch=models.CharField(choices=CB,max_length=29,default='X')
    def __str__(self):
        return self.School
    def __str__(self):
        return self.user.username



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

'''@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()'''


class Complaint(models.Model):
    STATUS =((1,'Solved'),(2, 'InProgress'),(3,'Pending'))
    TYPE=(('Can you help me understand the different career paths available for someone with my interests?',"Can you help me understand the different career paths available for someone with my interests?"),('What skills are most important for success in my desired career, and how can I develop them while still in school?',"What skills are most important for success in my desired career, and how can I develop them while still in school?"),('Are there any extracurricular activities or volunteer opportunities you recommend that align with my career goals?',"Are there any extracurricular activities or volunteer opportunities you recommend that align with my career goals?"),('How important is networking in my future career, and what steps can I take now to build connections?',"How important is networking in my future career, and what steps can I take now to build connections?"),('Other',"Other"))

    Subject=models.CharField(max_length=200,blank=False,null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE,default=None)

    Type_of_complaint=models.CharField(choices=TYPE,null=True,max_length=200)
    Description=models.TextField(max_length=4000,blank=False,null=True)
    Time = models.DateField(auto_now=True)
    status=models.IntegerField(choices=STATUS,default=3)


    def __init__(self, *args, **kwargs):
        super(Complaint, self).__init__(*args, **kwargs)
        self.__status = self.status

    def save(self, *args, **kwargs):
        if self.status and not self.__status:
            self.active_from = datetime.now()
        super(Complaint, self).save(*args, **kwargs)

    def __str__(self):
     	return self.get_Type_of_complaint_display()
    def __str__(self):
 	    return str(self.user)

    def __str__(self):
        return self.Subject

class Reply(models.Model):
    complaint = models.ForeignKey(Complaint, related_name='replies', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reply_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reply by {self.user.username} on {self.timestamp}"

class Grievance(models.Model):
    guser=models.OneToOneField(User,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.guser