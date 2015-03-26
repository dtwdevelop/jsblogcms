from blog.models import Category
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

class User():
    class Meta:
        content_type = ContentType.objects.get_for_model(Category)
#         permission = Permission.objects.create(codename='can_publish',
#                                        name='Can Publish Posts',
#                                        content_type=content_type)