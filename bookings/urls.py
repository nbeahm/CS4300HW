from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, SeatViewSet, BookingViewSet, api_home
from . import views


router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    
    path('', api_home, name='homepage'),
    path('api/', include(router.urls)),
    path('bookings/', views.booking_history_view, name='booking_history'),
    path('book/<int:movie_id>/', views.seat_booking_view, name='book_seat'),
    path('movies/', views.movie_list_view, name='movie_list')


]