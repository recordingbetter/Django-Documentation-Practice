from django.db import models


class CommonInfo2(models.Model):
    name = models.CharField(max_length = 100)
    age = models.PositiveIntegerField()

    class Meta:
        ordering = ('-name',)
        db_table = 'introduction_to_models_mti_commoninfo2'


class Student2(CommonInfo2):
    home_group = models.CharField(max_length = 5)

    def __str__(self):
        return 'HomeGroup {}\'s student({}, {}) pk={}'.format(
            self.home_group,
            self.name,
            self.age,
            self.pk,
        )

    class Meta:
        db_table = 'introduction_to_models_mti_student2'


class Teacher2(CommonInfo2):
    cls = models.CharField(max_length = 20)

    def __str__(self):
        return 'Class {} \'s teacher ({}, {}) pk={}'.format(
            self.cls,
            self.name,
            self.age,
            self.pk,
        )

    class Meta:
        db_table = 'introduction_to_models_mti_teacher2'
