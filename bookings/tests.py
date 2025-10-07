from django.test import TestCase
from .models import Movie, Seat, Booking
from datetime import date

class BookingModelTests(TestCase):
    def setUp(self):
        # Create a seat and a movie linked to that seat
        self.seat = Seat.objects.create(seat_number="A1", is_booked=False)
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="A test movie.",
            release_date=date(2025, 10, 6),
            duration=120,
            seat_set=self.seat
        )

    def test_seat_and_movie_creation(self):
        self.assertEqual(self.seat.seat_number, "A1")
        self.assertEqual(self.movie.title, "Test Movie")
        self.assertEqual(self.movie.seat_set, self.seat)

    def test_successful_booking(self):
        booking = Booking.objects.create(movie=self.movie, seat=self.seat)
        self.assertEqual(booking.movie.title, "Test Movie")
        self.assertEqual(booking.seat.seat_number, "A1")
        self.assertTrue(isinstance(booking.booking_date, type(self.movie.release_date)))

    def test_seat_marked_as_booked(self):
        Booking.objects.create(movie=self.movie, seat=self.seat)
        self.seat.refresh_from_db()
        self.seat.is_booked = True
        self.seat.save()
        self.assertTrue(self.seat.is_booked)

    def test_prevent_double_booking(self):
        Booking.objects.create(movie=self.movie, seat=self.seat)
        self.seat.is_booked = True
        self.seat.save()

        # Attempt second booking
        double_booking = Booking.objects.filter(movie=self.movie, seat=self.seat).count()
        self.assertEqual(double_booking, 1)