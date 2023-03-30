"""
Models for User Account

- The username is the Email and not a name.
- The user is staff
"""

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
# from datetime import datetime
import os
# from pytz import timezone
from phonenumber_field.modelfields import PhoneNumberField
from siraiitm.utils import OverwriteStorage, ImageTag
from django.utils import timezone



class UserManager(BaseUserManager):
	use_in_migrations = True

	def _create_user(self, email, password, **extra_fields):

		if not email:
			raise ValueError('Email is required')

		email = self.normalize_email(email)
		user = self.model(email=email, username=email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, email, password=None, **extra_fields):

		extra_fields.setdefault('is_superuser', False)
		return self._create_user(email, password, **extra_fields)

	def create_superuser(self, email, password, **extra_fields):

		extra_fields.setdefault('is_superuser', True)
		extra_fields.setdefault('is_staff', True)

		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser need to be is_superuser=True')

		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser need to be is_staff=True')

		return self._create_user(email, password, **extra_fields)


# Give image path with name as username
def get_profile_image_upload_path(instance, filename):
	__, img_extension = os.path.splitext(filename)
	return f'images/profile/{str(instance.username)}{str(img_extension)}'

class CustomUser(AbstractUser):

	email = models.EmailField('IITM Email', unique=True)
	# username = None
	USERNAME_FIELD = 'email'
	# REQUIRED_FIELDS = ['first_name', 'last_name']

	def __str__(self):
		return self.email

	objects = UserManager()
	# username = models.EmailField('IITM Email', unique=True)
	mobile = PhoneNumberField('Phone', unique=True, region='IN', null=True, blank=True)
	personal_email = models.EmailField('Personal Email', unique=True, null=True)
	REQUIRED_FIELDS = []
	date_of_birth = models.DateField(null=True, blank=True)

	class Gender(models.TextChoices):
		MALE = 'M', _('Male')
		FEMALE = 'F', _('Female')
		OTHERS = 'O', _('Others')
	gender = models.CharField(
		max_length=1,
		choices=Gender.choices,
		default=Gender.MALE,
		null=True, blank=True
	)
	photo = models.ImageField(upload_to=get_profile_image_upload_path, storage=OverwriteStorage, default='images/default/default_user.png')
	is_on_break = models.BooleanField(default=True)
	is_phone_verified = models.BooleanField('Verified', default=False)
	is_staff = models.BooleanField('Admin', default=False,
				help_text='Designated if the user is a team member')
	# address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
	last_updated = models.DateTimeField('Last updated', default=timezone.now,
				    null=True, blank=True)
	
	def __str__(self): return str(self.username)
	
	def save(self, *args, **kwargs):
		self.last_updated = timezone.now()
		super(CustomUser, self).save(*args, **kwargs)

	def image_tag(self):
		return ImageTag(self.photo)
	image_tag.allow_tags = True
	image_tag.__name__ = 'Photo'
	








"""
Models for User Account

- The username is the Email and not a name.
- The user is staff
"""

# from django.db import models
# from django.contrib.auth.models import AbstractUser, UserManager
# from django.utils.translation import gettext_lazy as _
# # from datetime import datetime
# import os
# # from pytz import timezone
# from phonenumber_field.modelfields import PhoneNumberField
# from siraiitm.utils import OverwriteStorage, ImageTag
# from django.utils import timezone



# class UserManager(BaseUserManager):
# 	use_in_migrations = True
# 	"""
#     Custom user model manager where email is the unique identifiers
#     for authentication instead of usernames.
#     """
# 	def create_user(self, username, password, **extra_fields):
# 		"""
# 		Create and save a User with the given phone and password.
# 		"""
# 		extra_fields.setdefault('is_superuser', False)
# 		extra_fields.setdefault('is_active', True)
# 		if not username:
# 			raise ValueError(_('The Phone number must be set'))
# 		user = self.model(username=username, **extra_fields)
# 		user.set_password(password)
# 		user.save()
# 		return user

# 	def create_superuser(self, username, password, **extra_fields):
# 		"""
# 		Create and save a SuperUser with the given email and password.
# 		"""
# 		extra_fields.setdefault('is_staff', True)
# 		extra_fields.setdefault('is_superuser', True)
# 		extra_fields.setdefault('is_active', True)

# 		if extra_fields.get('is_staff') is not True:
# 			raise ValueError(_('Superuser must have is_staff=True.'))

# 		if extra_fields.get('is_superuser') is not True:
# 			raise ValueError(_('Superuser must have is_superuser=True.'))
# 		return self.create_user(username=username, password=password, **extra_fields)


# # Give image path with name as username
# def get_profile_image_upload_path(instance, filename):
# 	__, img_extension = os.path.splitext(filename)
# 	return f'images/profile/{str(instance.username)}{str(img_extension)}'
								

# class CustomUser(AbstractUser):
# 	username = models.EmailField('IITM Email', unique=True)
# 	mobile = PhoneNumberField('Phone', unique=True, region='IN', null=True, blank=True)
# 	email = models.EmailField('Personal Email', unique=True)
# 	objects = UserManager()
# 	USERNAME_FIELD = 'username'
# 	REQUIRED_FIELDS = []
# 	date_of_birth = models.DateField(null=True, blank=True)

# 	class Gender(models.TextChoices):
# 		MALE = 'M', _('Male')
# 		FEMALE = 'F', _('Female')
# 		OTHERS = 'O', _('Others')
# 	gender = models.CharField(
# 		max_length=1,
# 		choices=Gender.choices,
# 		default=Gender.MALE,
# 		null=True, blank=True
# 	)
# 	photo = models.ImageField(upload_to=get_profile_image_upload_path, storage=OverwriteStorage, default='images/default/default_user.png')
# 	is_on_break = models.BooleanField(default=True)
# 	is_phone_verified = models.BooleanField('Verified', default=False)
# 	is_staff = models.BooleanField('Admin', default=False,
# 				help_text='Designated if the user is a team member')
# 	# address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
# 	last_updated = models.DateTimeField('Last updated', default=timezone.now(),
# 				    null=True, blank=True)
	
# 	def __str__(self): return str(self.username)
	
# 	def save(self, *args, **kwargs):
# 		self.last_updated = timezone.now()
# 		super(CustomUser, self).save(*args, **kwargs)

# 	def image_tag(self):
# 		return ImageTag(self.photo)
# 	image_tag.allow_tags = True
# 	image_tag.__name__ = 'Photo'




