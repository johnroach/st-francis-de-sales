from django.db import models


class ConfigurationKey(models.Model):
    key = models.TextField()
    value = models.TextField()

    def __str__(self):
        return self.key
