from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class Account(AbstractBaseUser):
	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	username 				= models.CharField(max_length=30, unique=True)
	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)


	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	objects = MyAccountManager()

	def __str__(self):
		return self.email

	# For checking permissions. to keep it simple all admin have ALL permissons
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
	def has_module_perms(self, app_label):
		return True



class Profile(models.Model):
    Account = models.OneToOneField(Account, null=True, on_delete=models.CASCADE) 
    dob = models.DateField(max_length=8)    
    clocation = models.CharField(max_length=30)
    qualification = models.CharField(max_length=30)
    course = models.CharField(max_length=30)
    specialization = models.CharField(max_length=30)
    university = models.CharField(max_length=30)
    College = models.CharField(max_length=30)
    course_type = models.CharField(max_length=30)
    passing_year = models.CharField(max_length=30)
    experience = models.CharField(max_length=30)
    cctc = models.CharField(max_length=30)
    ectc = models.CharField(max_length=30)
    industry = models.CharField(max_length=30)
    skills = models.CharField(max_length=30)
    job_category = models.CharField(max_length=30)
    job_type = models.CharField(max_length=30)
	
def __str__(self):
	return self.dob


class Job(models.Model):

    job_title = models.CharField(max_length=30)
    job_description = models.CharField(max_length=30)
    job_location = models.CharField(max_length=30)
    company_name = models.CharField(max_length=30)
    Designation = models.CharField(max_length=30)
    qualification = models.CharField(max_length=30)
    course = models.CharField(max_length=30)
    specialization = models.CharField(max_length=30)
    course_type = models.CharField(max_length=30)
    passing_year = models.CharField(max_length=30)
    experience = models.CharField(max_length=30)
    salary = models.CharField(max_length=30)
    industry = models.CharField(max_length=30)
    skills = models.CharField(max_length=30)
    job_category = models.CharField(max_length=30)
    job_type = models.CharField(max_length=30)

    
    def __str__(self):
        return self.job_title