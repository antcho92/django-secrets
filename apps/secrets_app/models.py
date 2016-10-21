from __future__ import unicode_literals
from django.db import models
from ..login_reg_app.models import User
from django.utils.encoding import python_2_unicode_compatible

class SecretManager(models.Manager):
    def add_secret(self, form_data, user):
        if len(form_data['content']) == 0:
            return (False, "You cannot submit a blank secret")
        else:
            Secret.objects.create(content=form_data['content'], user=user)
            return (True, "Secret added to database")
    def delete_secret(self, secret_id, user_id):
        secret = Secret.objects.get(id=secret_id)
        if secret.user.id == user_id:
            print("passed validations, deleting secret, checking for likes")
            likes = Like.objects.filter(secret=secret).delete()
            secret.delete()
            return(True, 'Successfully deleted your secret')
        else:
            return(False, 'user did make secret')

class LikeManager(models.Manager):
    def add_like(self, secret_id, user_id):
        secret = Secret.objects.get(id=secret_id)
        user = User.objects.get(id=user_id)
        if len(Like.objects.filter(secret=secret, user=user)) == 0:
            print("adding a like to database")
            Like.objects.create(secret=secret, user=user)
            return (True, "You have successfully like a secret")
        else:
            return (False, "You have already liked this secret")

# Create your models here.
class Secret(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = SecretManager()
    def __str__(self):              # __unicode__ on Python 2
        return self.content
    # this works but I used related name instead
    # def likes(self):
    #     return len(Like.objects.filter(secret=self))

class Like(models.Model):
    secret = models.ForeignKey(Secret, related_name='likes')
    user = models.ForeignKey(User, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = LikeManager()
    def __str__(self):              # __unicode__ on Python 2
        return (self.secret['id'], self.user['id'])
