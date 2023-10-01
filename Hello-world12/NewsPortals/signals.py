from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from django.template.loader import render_to_string


from NewsPortals.models import PostCategory, User
from NewsPortal import settings


def send_notifications(preview, pk, title, subscribers):
    html_contect = render_to_string(
        'post_created_email.html',
        {
            'text': preview,
            'link': f'{settings.SITE_URL}/news/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )

    msg.attach_alternative(html_contect, 'text/html')
    msg.send()
@receiver(m2m_changed, sender=PostCategory)
def notify_about_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.category.all()
        subscribers_emails = []

        for cat in categories:
            subscribers = cat.subscribers.all()
            subscribers_emails += [s.email for s in subscribers]

        send_notifications(instance.preview(), instance.pk, instance.heading, subscribers_emails)



@receiver(post_save, sender=User)
def user_signed_up_(created, **kwargs):
    instance = kwargs['instance']
    if created:
        html_content = render_to_string(
            'email/welcome.html',
            {
                'text': f'{instance.username}, Ваша регистрация прошла успешна!'
            }
        )

    msg = EmailMultiAlternatives(
        subject='Добро пожаловать!',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[instance.email],
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()