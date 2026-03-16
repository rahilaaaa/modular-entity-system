from django.db import models
from product.models import Product
from course.models import Course
from common.models import TimeStampedModel

class ProductCourseMapping(TimeStampedModel):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    primary_mapping = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ["product", "course"]