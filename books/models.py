from django.db import models


class AbstractBaseModel(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(AbstractBaseModel):
    name = models.CharField(max_length=255)
    objects = models.Manager()

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'


class Language(AbstractBaseModel):
    name = models.CharField(max_length=255)
    objects = models.Manager()

    class Meta:
        verbose_name = 'Til'
        verbose_name_plural = 'Tillar'


class Book(AbstractBaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    scan = models.BooleanField(default=False)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    objects = models.Manager()

    class Meta:
        verbose_name = 'Kitob'
        verbose_name_plural = 'Kitoblar'


class Discuss(AbstractBaseModel):
    class Meta:
        verbose_name = 'Muhokama'
        verbose_name_plural = 'Muhokamalar'


class Magazine(AbstractBaseModel):
    class Meta:
        verbose_name = 'Jurnal'
        verbose_name_plural = 'Jurnallar'


class Abstract(AbstractBaseModel):
    class Meta:
        verbose_name = 'Avtoreferat'
        verbose_name_plural = 'Avtoreferatlar'
