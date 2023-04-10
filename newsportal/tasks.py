import time

from celery import shared_task

from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string
import datetime
from News import settings
from newsportal.models import Post, PostCategory, Category


@shared_task
def send_notifications(preview, pk, title, subscribers):
    html_content = render_to_string(
        'post_create_email.html',
        {
            'text': preview,
            'link': f'{settings.SITE_URL}/news/{pk}',
        }
    )

    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@shared_task
def hello():
    time.sleep(10)
    print("Hello World!")


@shared_task
def my_job():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(dateCreation__gte=last_week)
    categories = set(posts.values_list('postCategory__name', flat=True))
    subscribers = set(Category.objects.filter(name__in=categories).values_list('subscribers__email', flat=True))
    html_content = render_to_string(
        "daily_post.html",
        {
            "link": settings.SITE_URL,
            "posts": posts,
        }
    )

    msg = EmailMultiAlternatives(
        subject="Наши новые публикации",
        body="",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()

