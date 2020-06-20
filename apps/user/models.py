from .base import AbstractEmailUser
from django.db import models


class User(AbstractEmailUser):
    first_name = models.CharField(max_length=30, default='')
    last_name = models.CharField(max_length=30, default='')
    

    def get_full_name(self):
        #return self.first_name + ' ' + self.last_name
        return '{} {}'.format(self.first_name, self.last_name) 
    get_full_name.short_description = 'name'


    def get_short_name(self):
        return self.first_name

