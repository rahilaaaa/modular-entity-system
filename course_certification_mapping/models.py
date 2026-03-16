from django.db import models
from course.models import Course
from certification.models import Certification
from common.models import TimeStampedModel

class CourseCertificationMapping(TimeStampedModel):

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    certification = models.ForeignKey(Certification, on_delete=models.CASCADE)

    primary_mapping = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ["course", "certification"]