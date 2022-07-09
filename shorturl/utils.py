from django.conf import settings
from random import choice
from string import ascii_letters, digits

SIZE = getattr(settings, "MAZIMUM_URL_CHARS", 6)

AVAILABLE_CHARS = ascii_letters + digits


def create_random_string(chars=AVAILABLE_CHARS):
    """Creates a random string with the predetermined size"""

    return "".join([choice(chars) for _ in range(SIZE)])


def shorten_url(model_instance):
    """Creates a shortened url and checks that it is unique"""

    random_string = create_random_string()
    model_class = model_instance.__class__

    if model_class.objects.filter(short_url=random_string).exists():
        return shorten_url(model_instance)

    return random_string
