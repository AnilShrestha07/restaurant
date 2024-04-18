from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.homepage, name='home'),
    path('food_detail/<int:food_id>/', views.food_detail, name='food_detail'),  # Include food_id parameter
    path('add-to-cart/<int:food_id>/', views.add_to_cart, name='add_to_cart'), # Include food
    path('change-quantity/<str:food_id>/', views.change_quantity, name='change_quantity'), #
    path('remove-from-cart/<str:food_id>/', views.remove_from_cart, name='remove_from_cart'), #
    path('cart/', views.cart_view, name='cart_view'), #
    path('logout/', views.logout_view, name='logout'), #
    path('checkout/', views.order, name='checkout'),
    path('about/', views.about, name='about-us'),
    path('book-table/', views.book_table, name='book_table'),
    path('booking-success/', views.booking_success, name='booking_success'),
    
]