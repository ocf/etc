from datetime import date
from datetime import datetime
from datetime import time
from datetime import timedelta

from ocflib.lab.hours import read_hours_listing


def test_hours_listing():
    hours_listing = read_hours_listing()

    today = date.today()

    # Make sure that calling functions doesn't cause exceptions, now or in the
    # future
    for i in range(100):
        hours_listing.hours_on_date(today + timedelta(days=i))
        hours_listing.hours_on_date(today - timedelta(days=i + 1))

        # Try every 10 minute interval on each day
        for j in range(timedelta(days=1) // timedelta(minutes=10)):
            fake_now = datetime.combine(
                today + timedelta(days=i), time(),
            ) + j * timedelta(minutes=10)

            hours_listing.is_open(when=fake_now)
            hours_listing.time_to_open(when=fake_now)
            hours_listing.time_to_close(when=fake_now)
