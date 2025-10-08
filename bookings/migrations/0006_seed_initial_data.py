from django.db import migrations
import datetime

def create_initial_data(apps, schema_editor):
    Seat = apps.get_model('bookings', 'Seat')
    Movie = apps.get_model('bookings', 'Movie')
    Booking = apps.get_model('bookings', 'Booking')

    # Create a seat
    seat = Seat.objects.create(seat_number="A1", is_booked=False)

    # Create a movie linked to that seat
    movie = Movie.objects.create(
        title="Test Movie",
        description="A default test movie.",
        release_date=datetime.date(2025, 10, 7),
        duration=120,
        seat_set=seat
    )

    # Create a booking
    Booking.objects.create(movie=movie, seat=seat)

def remove_initial_data(apps, schema_editor):
    Movie = apps.get_model('bookings', 'Movie')
    Movie.objects.filter(title="Test Movie").delete()

class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0005_remove_movie_seat_set_movie_seat_set'),
    ]

    operations = [
        migrations.RunPython(create_initial_data, reverse_code=remove_initial_data),
    ]


