from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(verbose_name="name", max_length=50, null=False, blank=False)
    email = models.EmailField(verbose_name="email", max_length=60)
    comment = models.CharField(verbose_name="comment", max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name