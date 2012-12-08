from django.db import models


class GiantSlalomEquipment(models.Model):
    name = models.CharField(max_length=50)
    multiplier = models.DecimalField(max_digits=6, decimal_places=4)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name


class JumpEquipment(models.Model):
    name = models.CharField(max_length=50)
    multiplier = models.DecimalField(max_digits=6, decimal_places=4)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name
