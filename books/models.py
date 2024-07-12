from django.db import models


class AbstractBaseModel(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Book(AbstractBaseModel):
    scan = models.BooleanField(default=False)


class Discuss(AbstractBaseModel):
    pass


class Magazine(AbstractBaseModel):
    pass
