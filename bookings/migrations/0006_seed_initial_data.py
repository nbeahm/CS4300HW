from django.db import migrations
import datetime

def create_initial_data(apps, schema_editor):
    Seat = apps.get_model('bookings', 'Seat')
    Movie = apps.get_model('bookings', 'Movie')
    Booking = apps.get_model('bookings', 'Booking')

    # Create a seat
    seat1 = Seat.objects.create(seat_number="1", is_booked=False)
    seat2 = Seat.objects.create(seat_number="2", is_booked=True)
    # Create a movie linked to that seat
    movie = Movie.objects.create(
        title="Test Movie",
        description="A default test movie.",
        release_date=datetime.date(2025, 10, 7),
        duration=120,
        seat_set=seat1
    )

    # Create a booking
    Booking.objects.create(movie=movie, seat=seat2)

def remove_initial_data(apps, schema_editor):
    Movie = apps.get_model('bookings', 'Movie')
    Movie.objects.filter(title="Test Movie").delete()

class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),  # or your latest migration
    ]

    operations = [
        migrations.RunPython(create_initial_data, reverse_code=remove_initial_data),
    ]