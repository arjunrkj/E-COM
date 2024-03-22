from django.db import models

class Collection(models.Model):
    collection_name = models.CharField(max_length=100)
    cover_img = models.ImageField(upload_to='collection_covers/')
    
    def __str__(self):
        return self.collection_name

class Product(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE,'Live'),(DELETE,'Delete'))
    
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='media/')
    delete_status = models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    priority = models.IntegerField(default=0) 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='shirts', null=True)
    # This creates a many-to-one relationship between Shirt and Collection

    def __str__(self):
        return self.title
