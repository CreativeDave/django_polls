<<<<<<< HEAD
from django.db import models
=======
import datetime

from django.db import models
from django.utils import timezone
>>>>>>> django polls basic UI added and test views added


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

<<<<<<< HEAD
=======
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

>>>>>>> django polls basic UI added and test views added

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
<<<<<<< HEAD
=======

    def __str__(self):
        return self.choice_text
>>>>>>> django polls basic UI added and test views added
