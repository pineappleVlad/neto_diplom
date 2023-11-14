from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.core.mail import EmailMessage
from django.dispatch import receiver, Signal
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django_rest_passwordreset.signals import reset_password_token_created

from .models import User

new_user_registered = Signal()
new_order = Signal()


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, **kwargs):
    """
    Отправляем письмо с токеном для сброса пароля
    When a token is created, an e-mail needs to be sent to the user
    :param sender: View Class that sent the signal
    :param instance: View Instance that sent the signal
    :param reset_password_token: Token Model Object
    :param kwargs:
    :return:
    """
    # send an e-mail to the user
    print(reset_password_token.key)
    msg = EmailMultiAlternatives(
        # title:
        f'{settings.URL_DOMAIN} Password Reset Token for {reset_password_token.user.last_name} \
{reset_password_token.user.first_name}.',
        # message:
        f'User: {reset_password_token.user.last_name} {reset_password_token.user.first_name}\nYour Reset Token:\
{reset_password_token.key}\n\nНе отвечайте на это письмо, оно создано автоматически)).',
        # from:
        settings.EMAIL_HOST_USER,
        # to:
        [reset_password_token.user.email]
    )
    msg.send()


@receiver(new_user_registered)
def new_user_registered_signal(user, user_password, **kwargs):
    id_encoded = urlsafe_base64_encode(force_bytes(user.id))
    print(id_encoded)
    msg = EmailMultiAlternatives(
        # title:
        f'Your Account activation: {settings.URL_DOMAIN}.',
        # message:
        f'Email: {user.user_email}\nPassword:{user_password} \n\n   Your Activation Link:http://\
{settings.URL_DOMAIN}/api/v1/user/register/confirm/?key={id_encoded}\n\nНе отвечайте на это письмо, оно создано \
автоматически)).',
        # from:
        settings.EMAIL_HOST_USER,
        # to:
        [user.email]
    )
    msg.send()


@receiver(new_order)
def new_order_signal(user_id, **kwargs):
    """
    отправяем письмо при изменении статуса заказа
    """
    # send an e-mail to the user
    user = User.objects.get(id=user_id)

    msg = EmailMultiAlternatives(
        # title:
        f"Обновление статуса заказа",
        # message:
        'Заказ сформирован',
        # from:
        settings.EMAIL_HOST_USER,
        # to:
        [user.email]
    )
    msg.send()