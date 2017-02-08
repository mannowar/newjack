from django.db import models
import datetime
from django.core.urlresolvers import reverse
from django.conf import settings

# Create your models here.
class Person(models.Model):
    '''Look at BaseUserManager to figure out password'''

    creation_date = models.DateTimeField(auto_now_add=True, auto_now=False)  # only when created, never overwritten
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)  # can be saved over
    email = models.EmailField(unique=True, blank=True, null=True)
    username = models.CharField(max_length=60, unique=True, blank=True, null=True)

    def __unicode__(self):
        return  "{}, <{}>".format(self.username, self.email)


class Contact(models.Model):
    '''Look at BaseUserManager to figure out password'''
    creation_date = models.DateTimeField(auto_now_add=True, auto_now=False)  # only when created, never overwritten
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)  # can be saved over
    email = models.EmailField(unique=True, blank=True, null=True)
    message = models.TextField(verbose_name="Message", blank=True)
    first_name = models.CharField("first name", max_length=255, blank=True)
    last_name = models.CharField("last name", max_length=255, blank=True)


    def __unicode__(self):
        return  "{}, <{}>".format(self.username, self.email)


class UserMusic(models.Model):
    '''Look at BaseUserManager to figure out password'''
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    creation_date = models.DateTimeField(auto_now_add=True, auto_now=False)  # only when created, never overwritten
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)  # can be saved over
    song_title = models.CharField(verbose_name="Song Title", max_length=255, blank=False)


    def __unicode__(self):
        return  "{}".format(self.user)

    def get_absolute_url(self):
        return reverse("UserHomePage", kwargs={"user": self.user})



# created = models.DateField(default=datetime.date.today)

# member_joined = models.DateField(blank=True, null=True)
# email_optout = models.BooleanField(default=False)
# obscode = models.CharField(max_length=6, unique=True, blank=True,
# null=True, validators=[validators.validate_obscode])

# password
# timestamp
# address2 = models.CharField("street address line 2", max_length=255,
#                           blank=True)
# city = models.CharField("city / town", max_length=255, blank=True)
# region = models.CharField("state / province / region", max_length=32,
#                          blank=True, help_text='Use two-letter state/province code in US/Canada')
# postal = models.CharField("ZIP / postal code", max_length=32, blank=True)
# country = models.CharField(max_length=3, choices=constants.COUNTRIES,
#                           blank=True)
# is_staff = models.BooleanField(
#    'admin status',
#    db_column='is_admin',
#    default=False,
#    help_text="Designates whether the user can log into this admin site."
# )

# Misc info
# latitude = models.FloatField(blank=True, null=True,
#                             validators=[validators.RangeValidator(-90, 90)])
# longitude = models.FloatField(blank=True, null=True,
#                             validators=[validators.RangeValidator(-180, 180)])
