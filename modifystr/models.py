from django.db import models

# Create your models here.
class ModifyStr(models.Model):
    original_string = models.CharField(max_length=300)
    new_string = models.CharField(max_length=300)
    method = models.CharField(max_length=50)
    class Meta:
        db_table = 'modify_str'