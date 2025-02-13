from django.db import models


# Create your models here.
class CombinationGroupNames(models.Model):
    groupName = models.CharField(max_length=100)

    def __str__(self):
        return str(self.groupName)


class CombinationGrouperChangers(models.Model):
    groupName = models.ForeignKey(CombinationGroupNames, on_delete=models.CASCADE)
    planetName = models.CharField(max_length=100)
    planetChangedName = models.CharField(max_length=100)

    def __str__(self):
        return str(self.planetName)


class Model1Charts(models.Model):
    dateLis = models.TextField(max_length=2000)
    m1ChartName = models.CharField(max_length=100)
    birthTime = models.CharField(max_length=100)
    p1Place = models.CharField(max_length=100)
    p2Place = models.CharField(max_length=100)

    def __str__(self):
        return self.m1ChartName


class Model2Charts(models.Model):
    dateLis = models.TextField(max_length=2000)
    m2ChartName = models.CharField(max_length=100)
    p1Time = models.CharField(max_length=100)
    p1Place = models.CharField(max_length=100)
    fName = models.CharField(max_length=100)
    p2Date = models.CharField(max_length=100)
    p2Time = models.CharField(max_length=100)
    p2Place = models.CharField(max_length=100)

    def __str__(self):
        return self.m2ChartName

class TrendChart4(models.Model):
    chartName = models.CharField(max_length=100)
    nameLis = models.CharField(max_length=100)
    combinations = models.CharField(max_length=100)
    data = models.TextField(blank=True, null=True, default='{}')

    def __str__(self):
        return self.chartName

class TrendChart1(models.Model):
    chartName = models.CharField(max_length=100)
    dateLis = models.CharField(max_length=100)
    combinations = models.CharField(max_length=100)
    data = models.TextField(blank=True, null=True, default='{}')

    def __str__(self):
        return self.chartName

class TrendChart2(models.Model):
    chartName = models.CharField(max_length=100)
    dateLis = models.CharField(max_length=100)
    combinations = models.CharField(max_length=100)
    data = models.TextField(blank=True, null=True, default='{}')

    def __str__(self):
        return self.chartName

class TrendChart3(models.Model):
    chartName = models.CharField(max_length=100)
    dateLis = models.CharField(max_length=100)
    combinations = models.CharField(max_length=100)
    data = models.TextField(blank=True, null=True, default='{}')

    def __str__(self):
        return self.chartName