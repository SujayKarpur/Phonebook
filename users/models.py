from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    image = models.ImageField(default = 'default.jpeg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def __save__(self):
        super().save()

        img = Image.open(self.image.path)
        
        if img.height>300 or img.width>300 : 
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
