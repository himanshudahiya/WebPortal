from django.db import models
from datetime import datetime 
# Create your models here.

class users(models.Model):
	user_name = models.CharField(max_length=250,default='')
	user_email = models.CharField(max_length=250,default='')
	user_mobile = models.IntegerField(default=0)
		

class lostEntry(models.Model):
	lost_item_name = models.CharField(max_length=250)
	lost_item_desc = models.CharField(max_length=2000, default='')
	lost_item_image = models.FileField()
	lost_item_place = models.CharField(max_length=1000,default='')
	lost_item_date_time = models.DateTimeField(default=datetime.now, blank=True)
	lost_item_post_time = models.DateTimeField(default=datetime.now, blank=True)
	user_pk = models.ForeignKey(users,on_delete=models.CASCADE)

class foundEntry(models.Model):
	found_item_name = models.CharField(max_length=250)
	found_item_desc = models.CharField(max_length=2000,default='')
	found_item_image = models.FileField()
	found_item_place = models.CharField(max_length=1000,default='')
	found_item_date_time = models.DateTimeField(default=datetime.now, blank=True)
	found_item_post_time = models.DateTimeField(default=datetime.now, blank=True)
	user_pk = models.ForeignKey(users,on_delete=models.CASCADE)
