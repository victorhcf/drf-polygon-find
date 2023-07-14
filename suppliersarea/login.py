from django.contrib.auth.models import User
from django.test import Client


def login(self, data):
    """
    Login function created to allow to authenticate user when running unit tests
    """
    self.username = 'dummy' + data + '@mail.com'
    self.password = 'dummy123'
    user = User.objects.create(username=self.username)
    user.set_password(self.password)
    user.save()

    c = Client()
    c.login(username=self.username, password=self.password)
    return c, user