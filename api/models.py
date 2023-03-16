from django.db import models



class DrugCategories(models.Model):
    cat_name = models.CharField(max_length=100)

    def __str__(self):
        return self.cat_name
    

class DrugClasses(models.Model):
    class_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.class_name
    

class Drugs(models.Model):

    AVAILABLE = "AV"
    UNAVAILABLE = "UNAV"

    AVAILABILITY = [
        (AVAILABLE, "Available"),
        (UNAVAILABLE, "Unavailable")
    ]

    name = models.CharField(max_length=100)
    category = models.ForeignKey(DrugCategories, on_delete=models.CASCADE)
    drug_class = models.ForeignKey(DrugClasses, on_delete=models.CASCADE)
    price = models.IntegerField(blank=True)
    description = models.TextField(max_length=500, blank=True)
    availability = models.CharField(max_length=20, choices=AVAILABILITY)

    def __str__(self):
        return self.name
    

class City(models.Model):
    city = models.CharField(max_length=15)
    code = models.SmallIntegerField(blank=True)

    def __str__(self):
        return self.city


class Pharmacy(models.Model):
    name = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Pharmacy"

    def __str__(self):
        return self.name