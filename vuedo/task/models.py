from django.db import models
from django.db.models.deletion import CASCADE


class Variable(models.Model):
    STRING = "string"
    BOOLEAN = "boolean"

    STATUS_CHOICES = ((STRING, "string"), (BOOLEAN, "boolean"))

    name = models.CharField(max_length=55)
    type = models.CharField(max_length=10, choices=STATUS_CHOICES, default=STRING)

    def __str__(self):
        return self.name


class BooleanValue(Variable):
    Value = models.BooleanField(default=False)


class StringValue(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name
