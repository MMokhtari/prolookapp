from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
import random
from AuthAccount.models import Account
from AuthAccount.models import Team
from django.core.validators import MaxValueValidator, MinValueValidator
import logging,sys

logger = logging.getLogger(__name__)
TASK_STATUS_CHOICES = (
    ('PENDING', 'Pending'),
    ('DONE', 'Done'),
    ('CANCELED', 'Canceled'),
    ('PROSTPOND', 'Prostpond'),
)
TASK_REPEAT_CHOICES = (('DAY','day'),('MONTH','Month'),)


# def random_color():
# 	"""
# 	Gets a random color code
# 	"""
#     color = '#%06X' % random.randint(0,256**3-1)
#     return color

class TaskTag(models.Model):
    title = models.CharField(max_length=30, blank=True, default='')
    description = models.CharField(max_length=60, blank=True, default='')
    color = models.CharField(max_length=20, blank=False, default='#342321')
    def __str__(self):
        return self.title

        
class Task(models.Model):
    account = models.ForeignKey(Account,null=True, blank=True, default = None)
    team = models.ForeignKey(Team,null=True, blank=True, default = None)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200, blank=True, default='Title')
    content = models.TextField(default='')
    status = models.CharField(choices=TASK_STATUS_CHOICES,max_length=20,null=True, blank=True)
    progression = models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(100)])
    due_date = models.DateTimeField(null=True, blank=True)
    is_repeatable = models.BooleanField(default=False)
    repeat_every = models.CharField(choices=TASK_REPEAT_CHOICES,max_length=20,null=True, blank=True)
    repeat_count = models.IntegerField(default=1,validators=[MinValueValidator(1)])
    is_event = models.BooleanField(default=False)
    is_prostpondable = models.BooleanField(default=True)
    is_referable = models.BooleanField(default=False)
    tags = models.ManyToManyField(TaskTag,null=True, blank=True,default = None)

    # #Overriding
    # def save(self,*args,**kwargs):
    #     #check if the row with this hash already exists.
    #     # logger.info('XXXXXXXXXXXXXXXXXXX')
    #     # tags = kwargs['tags']
    #     # del self[tags]
    #     # del kwargs[tags]
    #     tags = self.tags
    #     del self.tags
    #     self.content='The saver'
    #     self = super(Task, self).save(*args,**kwargs)
    #     # self.tags.add(tags)
    #     # super(Task, self).save()    

    def __str__(self):
        return self.title
    class Meta:
        ordering = ('created_at',)

class TaskTrack(models.Model):
    """Gets where is the task in case of referable task when the employee click on refer button"""
    task = models.ForeignKey(Task)
    refered_to = models.ForeignKey(Account)
    refered_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.task

class TaskReport(models.Model):
    """TaskReport model when thetask are done they have to have report"""
    created_at = models.DateTimeField(auto_now_add=True)
    task = models.ForeignKey(Task)
    title = models.CharField(max_length=30, blank=True, default='')
    content = models.TextField(default='')
    def __str__(self):
        return self.task
class TaskReportComment(models.Model):
    """docstring for TaskReportComment"""
    taskreport = models.ForeignKey(TaskReport)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=False)
    def __str__(self):
        return self.taskreport
class TaskComment(models.Model):
    """docstring for TaskComment"""
    task = models.ForeignKey(Task)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=False)
    def __str__(self):
        return self.task