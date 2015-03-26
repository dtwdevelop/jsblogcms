from django.db import models
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
import os
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from  web import settings
# Create your models here.
class Category(models.Model):
    
    title_category = models.CharField(max_length=150)
    post = models.TextField()
    tags = models.TextField()
    url = models.URLField(blank=True)
    hide= models.BooleanField(default=True)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.title_category
    
    def save(self, *args, **kwargs):
        self.url ="http://url.com/"
        super(Category, self).save(*args, **kwargs) 
        
    def get_absolute_url(self):
        
        return "/index?category={0}".format(self.title_category)
    
    class Meta:
        verbose_name = 'Categories'
        verbose_name_plural = 'Categories'
        ordering = ['-pub_date']
 
    
class Tag(models.Model):
    name = models.CharField(max_length=150)
    category_id = models.ForeignKey(Category)
    frequency = models.IntegerField()    
    def __unicode__(self):              # __unicode__ on Python 2
        return self.name
    
    def insert(self):
        pass
    
    def updateFrequency(self):
        pass
    
    def deleteTag(self):
        pass
    
class Page(models.Model):
    title=models.CharField(max_length=150,help_text="Title of you post")
    topic = models.TextField()
    category_id = models.ForeignKey(Category,related_name='pages')
    img_url =models.URLField(blank=True)
    hide =models.BooleanField(default=True)
    url = models.URLField(blank=True)
    pub_date = models.DateTimeField('date published')
    
class Gallery(models.Model):
    title = models.CharField(max_length=150,help_text="title")
    avatar = models.ImageField(upload_to='avatars')
    avatar_thumbnail = ImageSpecField(source='avatar',
                                      processors=[ResizeToFill(300, 200)],
                                      format='JPEG',
                                      options={'quality': 60})
    pos  = models.IntegerField()
    hide = models.BooleanField(default=True)
    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Gallery'
        
 
    
    
@receiver(pre_delete, sender = Gallery)
def delete_pic(instance, **kwargs):
    
    print(instance.avatar)
    url="{0}/{1}".format(settings.MEDIA_ROOT,instance.avatar) 
    os.remove(url)
    
    




class Comment(models.Model):
    title=models.CharField(max_length=150)
    page_id = models.ForeignKey(Page,related_name='comments')
    topic = models.TextField()
    category_id = models.ForeignKey(Category)
    hide =models.BooleanField(default=True)
    pub_date = models.DateTimeField('date published')
    
class Config(models.Model):  
    title =models.CharField(max_length=150)
    page_num =models.CharField(max_length=150)
    statu = models.BooleanField(default=True)
    meta_info = models.TextField()
    site_url =  models.URLField(blank=True)
    cache_time = models.IntegerField()
    
class Item(models.Model):
    title =models.CharField(max_length=150)
    item_url =  models.CharField(max_length=150)
    item_id =models.ForeignKey('self')
    hide = models.BooleanField(default=True)
    pos = models.IntegerField()
    
    def __unicode__(self):
        return self.title