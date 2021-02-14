from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    image = models.ImageField(default='default.jpg', upload_to='post_pics')
    content = models.TextField()
    publish = models.BooleanField(default=False)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

    def __str__(self):
    	return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


#comment model
class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    safe = models.BooleanField(default=False)

    def __str__(self):
        return self.author.username



#contacts	
class Contact(models.Model):
    email = models.CharField(max_length=100)
    message = models.TextField()
    subject = models.CharField(max_length=200)

    def __str__(self):
        return self.subject
