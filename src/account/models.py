from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from alireza.DjangoTools import rename_file

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
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        extra_fields.setdefault('first_name','your first name')
        extra_fields.setdefault('last_name','your last name')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)
    


def rename_profile_pic(instance,filename):
    return rename_file(instance,filename,hardpath='profile')


GENDERS = (
    ('none',_('هیچکدام')),
    ('male',_('مرد')),
    ('female',_('زن')),
)
class User(AbstractUser):
    """User model."""

    username = None
    first_name = models.CharField(_("first name"), max_length=40, blank=False,null=False)
    last_name = models.CharField(_("last name"), max_length=40, blank=False,null=False)
    email = models.EmailField(_('email address'), unique=True)

    #personal info
    gender = models.CharField('جنسیت',choices=GENDERS,max_length=7,default=('none','هیچکدام'),blank=True)
    image = models.ImageField('عکس',upload_to=rename_profile_pic,default='defaults/Default_Profile.png')
    company = models.CharField(_("کمپانی"),max_length=25,null=True,blank=True)
    area = models.CharField(_("منطقه"),max_length=25,null=True,blank=True)
    state= models.CharField(_("استان"),max_length=30,null=True,blank=True)
    city= models.CharField(_("شهر"),max_length=30,null=True,blank=True)
    street = models.CharField(_("خیابان"),max_length=80,null=True,blank=True)
    house_plate = models.SmallIntegerField(_("پلاک"),null=True,blank=True)
    zipcode = models.IntegerField(_("کد پستی"),null=True,blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(_("تلفن"),null=True,blank=True,validators=[phone_regex], max_length=17)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'





class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(to='products.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.title} - {self.user.email}"
    
    @property
    def complete_price(self):
        return self.product.discounted_price * self.quantity