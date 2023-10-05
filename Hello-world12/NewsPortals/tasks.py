from turtle import title

from celery import shared_task
import datetime

from django.core.mail import EmailMultiAlternatives

from NewsPortal import settings
from .models import Post, Category, PostCategory
from django.template.loader import render_to_string

@shared_task
def mail_task(pk):
    post = Post.objects.get(pk=pk)
    categories = post.category.all()
    heading = post.heading
    subscribers_emails = []
    for category in categories:
        subscribers_users = category.subscribers.all()
        for sub_user in subscribers_users:
            subscribers_emails.append(sub_user.email)
    html_content = render_to_string(
        'post_created.html',
        {
            'text': post.preview,
            'link': f'{settings.SITE_URL}/post/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers_emails,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()