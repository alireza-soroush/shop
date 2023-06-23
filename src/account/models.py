from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        extra_fields.setdefault('first_name','default first name')
        extra_fields.setdefault('last_name','default last name')
        extra_fields.setdefault('state','default state')
        extra_fields.setdefault('city','default city')
        extra_fields.setdefault('street','default street')
        extra_fields.setdefault('house_plate',1)
        extra_fields.setdefault('zipcode',1234)
        extra_fields.setdefault('phone',1234567890)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        extra_fields.setdefault('first_name','default first name')
        extra_fields.setdefault('last_name','default last name')
        extra_fields.setdefault('state','default state')
        extra_fields.setdefault('city','default city')
        extra_fields.setdefault('street','default street')
        extra_fields.setdefault('house_plate',0)
        extra_fields.setdefault('zipcode',1234)
        extra_fields.setdefault('phone',1234567890)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)
    

class User(AbstractUser):
    """User model."""

    username = None
    first_name = models.CharField(_("first name"), max_length=150, blank=False,null=False)
    last_name = models.CharField(_("last name"), max_length=150, blank=False,null=False)
    email = models.EmailField(_('email address'), unique=True)

    #personal info
    company = models.CharField(_("کمپانی"),max_length=25,null=True,blank=True)
    area = models.CharField(_("منطقه"),max_length=25,null=True,blank=True)
    state= models.CharField(_("استان"),max_length=30,null=False,blank=False,)
    city= models.CharField(_("شهر"),max_length=30,null=False,blank=False,)
    street = models.CharField(_("خیابان"),max_length=80,null=False,blank=False)
    house_plate = models.SmallIntegerField(_("پلاک"),null=False,blank=False)
    zipcode = models.IntegerField(_("کد پستی"),null=False,blank=False)
    phone = models.IntegerField(_("تلفن"),null=False,blank=False)
    cart = models.ManyToManyField(verbose_name=_("خرید ها"),to='products.Product',blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'