from django.db import models
class Seat(models.Model):
    seat_number = models.CharField(max_length=10)
    is_booked = models.BooleanField(default=False)
    def __str__(self):
        return f"Seat {self.seat_number} - {'Booked' if self.is_booked else 'Available'}"

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.IntegerField()# in minutes
    seat_set = models.ForeignKey(Seat, on_delete=models.CASCADE,)
    def __str__(self):
        return self.title





class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"booked seat {self.seat.seat_number} for {self.movie.title}"

