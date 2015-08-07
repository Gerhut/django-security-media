from django.db import models

from storages import security_storage

class Key(models.Model):

    public = models.FileField()
    private = models.FileField(storage=security_storage)

    class Meta:
        verbose_name = "Key"
        verbose_name_plural = "Keys"

    def __unicode__(self):
        return unicode(self.id)
