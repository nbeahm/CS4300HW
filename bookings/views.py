from django.shortcuts import render
import logging
from rest_framework import viewsets
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from django.shortcuts import redirect
from django.http import HttpResponseNotAllowed, JsonResponse
 


def redirect_to_api(request):
    if request.method == 'GET':
        return redirect('/api/')
    return HttpResponseNotAllowed(['GET'])


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

def movie_list_view(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})

def booking_history_view(request):
    bookings = Booking.objects.select_related('movie', 'seat').order_by('-booking_date')
    return render(request, 'bookings/booking_history.html', {'bookings': bookings})


def seat_booking_view(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    seats = Seat.objects.all()
    message = ''
    
    if request.method == 'POST':
        seat_id = request.POST.get('seat')
        seat = Seat.objects.get(id=seat_id)

        # Check if seat is already booked
        if Booking.objects.filter(movie=movie, seat=seat).exists():
            message = "That seat is already booked. Please choose another."

        else:
        # Create booking
            Booking.objects.create(movie=movie, seat=seat)
            bookings = Booking.objects.select_related('movie', 'seat').order_by('-booking_date')
            return render(request, 'bookings/booking_history.html', {'bookings': bookings})

    return render(request, 'bookings/seat_booking.html', {'movie': movie, 'seats': seats, 'message':message})

def api_home(request):
    return render(request, 'bookings/api_home.html')
