from django.db import models


class Restaurant(models.Model):
    dish_name = models.CharField(max_length=100)
    date = models.DateField()
    dish_type = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    seasonal = models.BooleanField(default=False)
    allergens = models.BooleanField(default=False)
    advance = models.BooleanField(default=False)
    img = models.ImageField(upload_to="pics/")
    comments = models.TextField()

    class Meta:
        db_table = "Rest"
