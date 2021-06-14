from django.db import models
from django.urls import reverse


from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.template.defaultfilters import slugify
# Create your models here.

class Blog(models.Model):
    title=models.CharField(max_length=200, unique=True)
    slug=models.SlugField(max_length=200, unique=True)
    description=models.TextField()
    name=models.CharField(max_length=30)
    created_on=models.DateTimeField('%Y-%m-%d %H:%M')


    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('blog',kwargs={'slug':self.slug})



    def save(self, *args, **kwargs): # new
        
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

'''def pre_save_post_receiver(sender, instance, *args, **kwargs):
    slug=slugify(instance.title)

    exists=Blog.objects.filter(slug=slug).exists()
    if exists:
        slug="%s-%s" %(slug, instance.id)
    instance.slug=slug

pre_save.connect(pre_save_post_receiver, sender=Blog)'''