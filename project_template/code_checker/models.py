from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User

from utils.models import DateTimeBase


class CodeCompile(DateTimeBase):
    """
    Every request to compile/run will be saved to this model.
    """
    LANGUAGE_CHOICE_C = 1
    LANGUAGE_CHOICE_PYTHON = 2
    LANGUAGE_CHOICE_RUBY = 3
    LANGUAGE_CHOICE_JAVA = 4

    LANGUAGE_CHOICES = (
        (LANGUAGE_CHOICE_C, 'C'),
        (LANGUAGE_CHOICE_PYTHON, 'Python'),
        (LANGUAGE_CHOICE_RUBY, 'Ruby'),
        (LANGUAGE_CHOICE_JAVA, 'Java'),
    )

    language = models.IntegerField(choices=LANGUAGE_CHOICES)
    source = models.TextField()
    test_cases = JSONField()
    user = models.ForeignKey(User)

    # Result
    stderr = models.TextField(null=True, blank=True)
    stdout = models.TextField(null=True, blank=True)
    time = models.DecimalField(
        decimal_places=4, max_digits=10, null=True, blank=True)
    is_correct = models.NullBooleanField()

    def __unicode__(self):
        return u"%s" % self.get_language_display()
