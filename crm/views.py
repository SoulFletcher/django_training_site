from django.shortcuts import render
from .models import Order
from .forms import OrderForm

def first_page(request):
    data = Order.objects.all()
    form = OrderForm()
    return render(request, 'index.html', {'data': data,
                                          'form': form})


def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    element = Order(order_name=name, order_phone=phone)
    element.save()
    return render(request, 'thanks_page.html', {'name': name,
                                                'phone': phone})
