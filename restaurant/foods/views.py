from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import OrderForm, BookingForm, Booking

from .cart import Cart

from .models import  Foods,Category

# Create your views here.

def homepage(request):
    category = request.GET.get('category')
    food = Foods.objects.all()
    
    if category == None:
        food = Foods.objects.all()
        category = Category.objects.all()
    else:
        food = Foods.objects.filter(category__name=category)
        category = Category.objects.all()
    
    return render(request, "home.html", {'food': food, 'category': category})



@login_required
def book_table(request):
    booking = Booking.objects.filter(user=request.user)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user_id = request.user.id
            booking.save()
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'book_table.html', {'form': form, 'booking':booking})

def checkout(request):
    pass
    
def booking_success(request):
    return render(request, 'booking_success.html')

def about(request):
    return render(request, "about.html")

def logout_view(request):
    logout(request)
    return redirect('login')
    

    
def food_detail(request):
    food = Foods.objects.all()
    return render(request, "food_detail.html", {'food': food})


def add_to_cart(request,food_id):
    cart = Cart(request)
    cart.add(food_id)
    
    return redirect('home')

def change_quantity(request,food_id):
    action = request.GET.get('action', '')    
    if action in ['increase', 'decrease']:
        quantity = 1 if action == 'increase' else -1
                  
        cart = Cart(request)
        cart.add(food_id, quantity,True)
    
    return redirect("cart_view")

def remove_from_cart(request,food_id):
    cart = Cart(request)
    cart.remove(food_id)
    
    return redirect("cart_view")

def cart_view(request):
    cart = Cart(request)
    return render(request, "cart_view.html", {'cart': cart}) 

def order(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    return render(request, 'checkout.html', {'form':form})




 
 
