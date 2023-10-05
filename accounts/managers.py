from django.contrib.auth.models import BaseUserManager


class UsersManager(BaseUserManager):
    def create_user(self, email, mobile_phone, full_name, password=None):
        if not email:
            raise ValueError('please provide an email address')
        if not mobile_phone:
            raise ValueError('please provide a mobile phone number')
        if not full_name:
            raise ValueError('please provide a full name')
        
        user = self.model(
            email=self.normalize_email(email),
            mobile_phone=mobile_phone,
            full_name=full_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, mobile_phone, full_name, password=None):
        user = self.create_user(
            email=email,
            mobile_phone=mobile_phone,
            full_name=full_name,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user