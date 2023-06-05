from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from website.forms import OrderForm
from website.models import Order

from website.auth.decorators import customer_required, supplier_required

def index(request):
    return render(request, 'landing.html')


@login_required
def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            Order.objects.create(
                customer=request.user, 
                status=Order.CREATED,
                tomato_type=form.cleaned_data['tomato_type']
            )

            return redirect("profile")
    else:
        form = OrderForm()

    return render(request, 'users/order_page.html', {'form' : form})


@login_required
def order_process(request):
    # create order
    Order.objects.create(customer=request.user, status=Order.CREATED)
    return redirect("index")


@login_required
def profile(request):
    orders = Order.objects.filter(customer=request.user).order_by('-timestamp')
    return render(request, 'users/profile.html', { 'orders' : orders })

@login_required
@supplier_required
def supplier_profile(request):
    usr = request.user
    print(usr.is_supplier)
    orders = Order.objects.order_by('-timestamp')#, supplier__isnull)    .filter(supplier__isnull=True)
    # orders_old = Order.objects.filter(supplier__isnull=False).order_by('-timestamp')

    return render(request, 'users/supplier_profile.html', { 'orders' : orders })
