

from django.contrib.auth.models import AbstractUser





class User(AbstractUser):
    @property
    def fullname(self):
        if self.first_name and self.last_name:
            return str(f"{self.first_name} {self.last_name}")
        elif self.first_name:
            return str(f"{self.first_name}")
        else:
            return self.username