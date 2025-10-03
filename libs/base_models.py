import datetime
import uuid

from django.db import models


class BaseModel(models.Model):
    id = models.CharField(primary_key=True, default=lambda: uuid.uuid1().hex, editable=False, max_length=32)
    created_at = models.DateTimeField(default=datetime.datetime.now)
    updated_at = models.DateTimeField(default=datetime.datetime.now)

    def save(
            self, *args,
            force_insert=False,
            force_update=False,
            using=None,
            update_fields=None,
    ):
        self.updated_at = datetime.datetime.now()
        return super().save(*args,
                            force_insert=force_insert,
                            force_update=force_update,
                            using=using,
                            update_fields=update_fields)

    class Meta:
        abstract = True
