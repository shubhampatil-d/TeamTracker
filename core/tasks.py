# core/tasks.py

# from celery import shared_task
# from django.core.mail import send_mail
# from django.contrib.auth import get_user_model
# from .models import Task

# @shared_task
# def send_task_reminder(task_id):
#     try:
#         task = Task.objects.get(id=task_id)
#         if task.assigned_to and task.assigned_to.email:
#             subject = f"Task Reminder: {task.title}"
#             message = f"""
# Hi {task.assigned_to.username},

# This is a reminder that your task "{task.title}" is due on {task.due_date}.

# Task Description:
# {task.description}

# Regards,
# TaskFlow
# """
#             send_mail(
#                 subject,
#                 message,
#                 'noreply@taskflow.com',
#                 [task.assigned_to.email],
#                 fail_silently=False
#             )
#     except Task.DoesNotExist:
#         pass
