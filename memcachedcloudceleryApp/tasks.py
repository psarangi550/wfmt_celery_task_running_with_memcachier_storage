from __future__ import absolute_import,unicode_literals
from django_celery_results.models import TaskResult
from django.core.cache import cache

from celery import shared_task

@shared_task
def add(a,b):
    task_result=TaskResult.objects.get(id=1)
    # print(task_result)
    cache.set("result",task_result)
    cache.get("result")
    return a+b