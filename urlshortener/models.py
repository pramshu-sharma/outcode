from django.db import models


class URLMapping(models.Model):
    url = models.URLField()
    hashed = models.CharField(max_length=25)
    create_ts = models.DateTimeField(auto_now_add=True)


