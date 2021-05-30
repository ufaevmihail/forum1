from django.db import models
from django.utils import timezone,dateformat
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User
import datetime
# Create your models here.


class UserProperties(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    admin = models.BooleanField(default=False)
    verified=models.BooleanField(default=False)


class Rubric(MPTTModel):
    user = models.ForeignKey(User, default = None,on_delete = models.CASCADE)

    name = models.CharField(max_length=100)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    banned = models.ManyToManyField(User,related_name="banned")
    moders = models.ManyToManyField(User,related_name="moders")


class Theme(models.Model):
    user = models.ForeignKey(User, default = None, on_delete = models.CASCADE)
    rubric = models.ForeignKey(Rubric, on_delete = models.CASCADE)
    name = models.CharField(max_length=30)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    last_update = models.DateTimeField(default=timezone.now)


class Comment(MPTTModel):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    theme = models.ForeignKey(Theme,on_delete = models.CASCADE)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def update_state(self):
        d=timezone.now()
        last_update = d.strftime("%Y-%m-%d %H:%M:%S")
        self.theme.last_update=last_update
        self.theme.save()


#class ModeratorIn(models.Model)




