from django.db import models

# Create your models here.
class DateLisDB(models.Model):
    datelis = models.TextField(max_length=2000)

    def __str__(self):
        return str(self.id) 

class PlanetChanger(models.Model):
    planetName = models.CharField(max_length=100)
    planetChangedName = models.CharField(max_length=100)

    def __str__(self):
        return str(self.planetName)

class PlanetGroupNames(models.Model):
    groupName = models.CharField(max_length=100)

    def __str__(self):
        return str(self.groupName)


class PlanetGroupers(models.Model):
    groupName = models.ForeignKey(PlanetGroupNames, on_delete=models.CASCADE)
    planetName = models.CharField(max_length=100)
    planetChangedName = models.CharField(max_length=100)

    def __str__(self):
        return str(self.planetName)


class MultiDateLisDB(models.Model):
    datelis = models.TextField(max_length=2000)

    def __str__(self):
        return str(self.id) 



    
class divisionName(models.Model):
    divName = models.CharField(max_length=100)

    def __str__(self):
        return self.divName

class modelNames(models.Model):
    modelcategory = models.ForeignKey(divisionName, on_delete=models.CASCADE)
    modelFullName = models.CharField(max_length=100)
    birthDateTime = models.CharField(max_length=100)
    modelLocation = models.CharField(max_length=100)

    def __str__(self):
        return (str(self.id))

class TrendCharts(models.Model):
    category = models.CharField(max_length = 100)
    cName = models.CharField(max_length = 100)
    cPlace = models.CharField(max_length = 100)
    cDate = models.CharField(max_length = 100)
    cTime = models.CharField(max_length = 100)

    def __str__(self):
        return self.cName

         