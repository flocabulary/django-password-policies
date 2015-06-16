import datetime
from django.utils import timezone

def datetime_to_timestamp(dt):
    if timezone.is_naive(dt):
        dt = timezone.make_aware(dt, timezone.get_default_timezone())
    epoch = timezone.make_aware(datetime.datetime.utcfromtimestamp(0), timezone.utc)
    delta = dt - epoch
    return int(delta.total_seconds())
