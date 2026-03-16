from django.db import models
from vendor.models import Vendor
from product.models import Product
from common.models import TimeStampedModel


class VendorProductMapping(TimeStampedModel):

    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    primary_mapping = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ["vendor", "product"]

    def __str__(self):
        return f"{self.vendor} -> {self.product}"