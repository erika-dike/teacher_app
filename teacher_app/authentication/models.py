from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Teacher(User):

    def __unicode__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)
