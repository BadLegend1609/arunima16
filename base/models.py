from django.db import models
from django.utils.text import slugify
from django.shortcuts import reverse 
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericRelation

import datetime

from hitcount.models import HitCountMixin, HitCount
from ckeditor_uploader.fields import RichTextUploadingField



# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Post(models.Model):
    thumbnail = models.ImageField(null=True, blank=True, upload_to='images', default='default.jpg')
    title = models.CharField(max_length = 50, blank=True)
    subtitle = models.CharField(max_length = 50, blank=True)
    content = RichTextUploadingField(max_length = 20000000000, blank=True)
    private = models.BooleanField(default=False)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    tag = models.ManyToManyField(Tag, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.title}{datetime.date.today()}{timezone.now()}')
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse("base:post", kwargs={
            "slug": self.slug
        })
    


class Me(models.Model):
    
    ## Header Section
    page_header_1 = models.CharField(max_length=200, null=True, blank=True, default="Header 1")
    page_sub_header_1 = models.CharField(max_length=200, null=True, blank=True, default="Sub Header 1")

    page_header_2 = models.CharField(max_length=200, null=True, blank=True, default="Header 2")
    page_sub_header_2 = models.CharField(max_length=200, null=True, blank=True, default="Sub Header 2")

    page_header_3 = models.CharField(max_length=200, null=True, blank=True, default="Header 3")
    page_sub_header_3 = models.CharField(max_length=200, null=True, blank=True, default="Sub Header 3")

    ## About Section
    who_am_i = RichTextUploadingField(max_length=5000, null=True, blank=True, default="Lorem ipsum dolor sit amet set, consectetur utes anet adipisicing elit, sed do eiusmod tempor incidist.")
    what_i_do = RichTextUploadingField(max_length=5000, null=True, blank=True, default="Lorem ipsum dolor sit amet set, consectetur utes anet adipisicing elit, sed do eiusmod tempor incidist.")
    why_i_do_it = RichTextUploadingField(max_length=5000, null=True, blank=True, default="Lorem ipsum dolor sit amet set, consectetur utes anet adipisicing elit, sed do eiusmod tempor incidist.")
    since_when = RichTextUploadingField(max_length=5000, null=True, blank=True, default="Lorem ipsum dolor sit amet set, consectetur utes anet adipisicing elit, sed do eiusmod tempor incidist.")

    ## Some Fun Facts Section
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')


    ## Social Section
    facebook_link = models.URLField(null=True, blank=True, default='https://facebook.com')
    twitter_link = models.URLField(null=True, blank=True, default='https://twitter.com')
    instagram_link = models.URLField(null=True, blank=True, default='https://instagram.com')
    pinrest_link = models.URLField(null=True, blank=True, default='https://pinterest.com')

    class Meta:
        verbose_name_plural = "Me"

    def __str__(self):
        return "Arunima"