from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from siraiitm.utils import OverwriteStorage, ImageTag
import os

# Create your models here.

def get_default_user_photo_image_upload_path(instance, filename):
	# __, img_extension = os.path.splitext(filename)
	# return f'images/profile/{str(instance.username)}{str(img_extension)}'
    return 'images/default/default_user.png'

def get_default_site_logo_image_upload_path(instance, filename):
	# __, img_extension = os.path.splitext(filename)
	# return f'images/profile/{str(instance.username)}{str(img_extension)}'
    return 'images/default/default_logo.png'

def get_default_site_favicon_image_upload_path(instance, filename):
	return 'images/default/favicon.png'

class Defaults(models.Model):
	class Meta:
		verbose_name_plural = "Default Site Properties"
	default_site_name = models.CharField('Site name', max_length=200, help_text='IIT Madras B.S Degree')
	default_portal_name = models.CharField('Portal name', max_length=200, null=True, blank=True)
	default_portal_shortform = models.CharField('ShortForm', max_length=20, null=True, blank=True)
	support_mobile = PhoneNumberField('Phone', unique=True, region='IN', null=True, blank=True)
	support_email = models.EmailField('Support Email', unique=True, null=True)
	default_user_photo = models.ImageField(upload_to=get_default_user_photo_image_upload_path, storage=OverwriteStorage)
	default_site_logo = models.ImageField(upload_to=get_default_site_logo_image_upload_path, storage=OverwriteStorage)
	default_site_favicon = models.ImageField(upload_to=get_default_site_favicon_image_upload_path, storage=OverwriteStorage)
	
	def __str__(self): return str(self.default_site_name)

	def default_user_photo_image_tag(self):
		return ImageTag(self.default_user_photo)
	def default_site_logo_image_tag(self):
		return ImageTag(self.default_site_logo)
	def default_site_favicon_image_tag(self):
		return ImageTag(self.default_site_favicon)
		
	# image_tag.allow_tags = True
	# image_tag.__name__ = 'Photo'
	