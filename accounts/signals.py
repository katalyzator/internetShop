import stripe

from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
from django.db.models.signals import post_save

from .models import UserStripe

stripe.api_key = settings.STRIPE_SECRET_KEY


def get_or_create_stripe(sender, user, *args, **kwargs):
    try:
        user.userstripe.stripe_id
    except UserStripe.DoesNotExist:
        customer = stripe.Customer.create(
            email=user.email
        )
        new_user_stripe = UserStripe.objects.create(
            user=user,
            stripe_id=customer.stripe_id
        )
    except:
        pass


user_logged_in.connect(get_or_create_stripe)


def test_past_save_signal(sender, instance, created, *args, **kwargs):
    print sender
    print instance
    print created


post_save.connect(test_past_save_signal, sender=User)
