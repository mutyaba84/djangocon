from django.db import models
from django.db.models.deletion import CASCADE


class Variable(models.Model):
    STRING = "string"
    DONE = "done"

    STATUS_CHOICES = ((STRING, "string"), (DONE, "Done"))

    name = models.CharField(max_length=255)
    type = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default=STRING)

    def __str__(self):
        return self.name


class BooleanValue(Variable):
    Value = models.BooleanField(default=False)


class StringValue(models.Model):
    Value = models.CharField(max_length=30)

    def __str__(self):
        return self.Value
