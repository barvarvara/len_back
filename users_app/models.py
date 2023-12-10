# from django.core.validators import RegexValidator
# from django.db import models
#
# from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin, AbstractUser
#
#
# # class UserAccountManager(BaseUserManager):
# #     def create_user(self, name, phone_number, email, password=None):
# #         if not email:
# #             raise ValueError("У пользователя должен быть email")
# #
# #         email = self.normalize_email(email).lower()
# #
# #         user = self.model(
# #             email=email,
# #             name=name,
# #             phone_number=phone_number
# #         )
# #
# #         user.set_password(password)
# #         user.save(using=self._db)
# #         return user
#
#
# phone_validator = RegexValidator(r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$")
#
#
# class UserAccount(AbstractUser, PermissionsMixin):
#     name = models.CharField(max_length=255)
#     email = models.EmailField(max_length=255, unique=True)
#     phone_number = models.CharField(max_length=14, validators=[phone_validator], unique=True, verbose_name='номер телефона')
#
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#
#     # objects = UserAccountManager()
#     # USERNAME_FIELD = 'phone_number'
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['phone_number', 'name']
#
#     def __str__(self):
#         return self.email
