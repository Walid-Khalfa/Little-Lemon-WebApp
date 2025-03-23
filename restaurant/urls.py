from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'menu', views.MenuViewSet)
router.register(r'booking', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('menu/<int:pk>/', views.display_menu_item, name='menu_item'),
    path('book/', views.book, name='book'),
    path('reservations/', views.reservations, name='reservations'),
    path('bookings', views.bookings, name='bookings'),
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Add this line for token authentication
]