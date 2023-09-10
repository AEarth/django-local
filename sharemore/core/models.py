from django.db import models

# Create your models here.
from django.db import models
# from toolshare.users.models import User

# import uuid

# # Create your models here.

# class Brand(models.Model):
#     brand = models.CharField(max_length = 25)
#     def __str__(self):
#         """String for representing the model Object"""
#         return f"test this {self.brand} brand"
  
# class ToolType(models.Model):
#     """Model representing various types of tools"""
#     toolname = models.CharField(max_length = 50)
#     brand = models.ForeignKey('Brand',on_delete=models.SET_NULL, null=True)
    
#     POWER_TYPE_CHOICES = (
#         ('g', 'gas'),
#         ('b', 'battery'),
#         ('w', 'wired'),
#     )
#     power_type = models.CharField(max_length=1, choices=POWER_TYPE_CHOICES, null=True)
    
#     def __str__(self):
#         """String for representing the model Object"""
#         return self.toolname
    

# class ToolInstance(models.Model):
#     """Model representing a specific tool"""
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular tool across whole app')
#     owner = models.ForeignKey('users.User',on_delete=models.SET_NULL, null=True)
#     tooltype = models.ForeignKey('ToolType', on_delete=models.SET_NULL, null=True)
#     description = models.CharField(max_length = 400)
    
#     def __str__(self):
#         """String for representing the model Object"""
#         return f"{self.tooltype} - {self.owner}"
  

# class LendAsk(models.Model):
#     requester = models.ForeignKey('users.User', on_delete=models.CASCADE)
#     tool = models.ForeignKey('ToolInstance', on_delete=models.CASCADE)
#     REQUEST_STATUS = (
#         ('p', 'Pending'),
#         ('a', 'Approved'),
#         ('d', 'Denied'),
#     )
#     status = models.CharField(max_length=1, choices=REQUEST_STATUS, default='p')

#     def __str__(self):
#         return f"{self.requester} - {self.get_status_display()} - {self.tool}"
  

# class LendPeriod(models.Model):
#     lend_request = models.OneToOneField('LendAsk', on_delete=models.CASCADE)
#     start_date = models.DateField(help_text='Start date of the lend')
#     end_date = models.DateField(help_text='End date of the lend')
    
#     # def __str__(self):
#     #     return f"{self.loan_request.tool} loaned from {self.start_date} to {self.end_date}"