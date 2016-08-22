from __future__ import unicode_literals

from django.contrib.auth.models import User

from django.db import models

from carts.models import Cart

STATUS_CHOICES = (
    ("Started", "Started"),
    ("Abandoned", "Abandoned"),
    ("Finished", "Finished"),
)


# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    cart = models.ForeignKey(Cart)
    order_id = models.CharField(max_length=120, default='ABC', unique=True)
    status = models.CharField(max_length=120, choices=STATUS_CHOICES, default="Started")
    # address
    sub_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)
    tax_total = models.DecimalField(default=0.00, max_digits=1000, decimal_places=2)
    final_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.order_id
