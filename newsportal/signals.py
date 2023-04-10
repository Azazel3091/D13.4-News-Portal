from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from .models import PostCategory, Post, Category
from django.conf import settings
from newsportal.tasks import send_notifications


@receiver(m2m_changed, sender=PostCategory)
def post_created(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        print('это сигнал!')
        categories = instance.postCategory.all()
        subscribers_email: list[str] = []
        for category in categories:
            print(f'{categories = }')
            subscribers = category.subscribers.all()
            subscribers_email += [s.email for s in subscribers]

        print(f'{subscribers = }')

        send_notifications.delay(instance.preview(), instance.pk, instance.title, subscribers_email)


        ########

# @receiver(post_save, sender=PostCategory)
# def post_created(sender, instance, created, **kwargs):
#     if created and instance.__class__.__name__ == 'Post':
#         categories = instance.post_category.all()
#         subscribers: list[str] = []
#         for category in categories:
#             subscribers += category.subscribers.all()
#
#         subscribers = [s.email for s in subscribers]
#
#         send_notifications.apply_async(instance.preview(), instance.pk, instance.title, subscribers, instance.id)
