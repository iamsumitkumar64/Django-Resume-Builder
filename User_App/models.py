from django.db import models

# Create your models here.
class user_data(models.Model):
    username = models.CharField(verbose_name="Enter UserName",max_length=15)

    intro_firstname = models.CharField(verbose_name="Enter FirstName",max_length=10)
    intro_middlename = models.CharField(verbose_name="Enter MiddleName",max_length=10)
    intro_lastname = models.CharField(verbose_name="Enter LastName",max_length=10)
    # intro_image = models.FileField(upload_to='user_images/',verbose_name="Enter User Image",max_length=100,null = True,default=None)
    intro_image=models.TextField(default="")
    intro_designation = models.CharField(verbose_name="Enter  Designation",max_length=10)
    intro_address = models.TextField(verbose_name="Enter User Address")
    intro_email = models.EmailField(verbose_name="Enter User Email")
    intro_phone = models.CharField(verbose_name="Enter User Mobile Number",max_length=13)
    intro_summary = models.CharField(verbose_name="Enter User Summary",max_length=50)

    achi_title = models.CharField(verbose_name="Enter  Achievement Title",max_length=20)
    achi_description = models.TextField(verbose_name="Enter  Achievement Description")

    exp_title = models.CharField(verbose_name="Enter  Experience Title",max_length=20)
    exp_company = models.CharField(verbose_name="Enter  Experience Company",max_length=20)
    exp_location = models.CharField(verbose_name="Enter  Experience Location",max_length=20)
    exp_start_date = models.JSONField(verbose_name="Enter  Experience Start Date")
    exp_end_date = models.JSONField(verbose_name="Enter  Experience End Date")
    exp_description = models.TextField(verbose_name="Enter  Experience Description")

    edu_school = models.CharField(verbose_name="Enter  Education School",max_length=20)
    edu_degree = models.CharField(verbose_name="Enter  Education Degree",max_length=20)
    edu_city = models.CharField(verbose_name="Enter  Education City",max_length=20)
    edu_start_date = models.JSONField(verbose_name="Enter  Education Start Date")
    edu_end_date = models.JSONField(verbose_name="Enter  Education End Date")
    edu_description = models.TextField(verbose_name="Enter  Education Description")

    proj_name = models.CharField(verbose_name="Enter  Project Name",max_length=20)
    proj_link = models.TextField(verbose_name="Enter  Project Link")
    proj_description = models.TextField(verbose_name="Enter  Project Description")

    skills = models.TextField(verbose_name="Enter skills")