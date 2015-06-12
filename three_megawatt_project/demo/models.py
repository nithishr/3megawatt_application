from django.db import models

# Create your models here.
class Site(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.name

class SiteDetail(models.Model):
    site = models.ForeignKey(Site)
    date = models.DateField()
    a_value = models.DecimalField(max_digits=6,decimal_places=3)
    b_value = models.DecimalField(max_digits=6,decimal_places=3)

    def __unicode__(self):
        return self.site.name
