# todo/todo_api/models.py
from django.db import models

class ShahihBukharis(models.Model):
    id = models.BigAutoField(primary_key=True)
    kitab = models.CharField(max_length=200)
    arab = models.TextField()
    terjemah = models.TextField()

    class Meta:
        managed = False
        db_table = 'shahih_bukharis'