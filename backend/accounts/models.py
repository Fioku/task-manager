from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission
# from django.utils import timezone

# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     is_active = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)

#     date_joined = models.DateTimeField(default=timezone.now)

#     groups = models.ManyToManyField(
#         Group,
#         related_name="accounts_users",
#         blank=True,
#     )
#     user_permissions = models.ManyToManyField(
#         Permission,
#         related_name="accounts_users_permissions",
#         blank=True,
#     )


#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name']

#     objects = models.Manager()

#     def __str__(self):
#         return self.email