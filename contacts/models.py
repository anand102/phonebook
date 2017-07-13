from __future__ import unicode_literals

from django.db import models

class Person(models.Model):
	username=models.CharField(max_length=50)
	password=models.CharField(max_length=50)

	def __str__(self):
		return self.username	

class Contact(models.Model):
	person=models.ForeignKey(Person,on_delete=models.CASCADE)
	name=models.CharField(max_length=30)
	number=models.CharField(max_length=30)

	def __str__(self):
		return self.name	
