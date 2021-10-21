from django.db import models


class Parent(models.Model):
    name = models.CharField(max_length=200, null=True)
    age = models.IntegerField
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Child(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(null=True)

    class Meta:
        verbose_name_plural = 'Children'

    def __str__(self):
        return self.name