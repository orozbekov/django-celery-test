from celery import shared_task
from django.core.mail import send_mail
from config import settings


@shared_task
def send_activation_code(absolute_link, email):
    message = f'Активируйте свой аккаунт, перейдя по ссылке:\n{absolute_link}'
    send_mail(
        subject="Activate account",
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email])
    return 'Done'