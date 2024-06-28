from django.shortcuts import render,redirect
from . models import Order,OrderedItem
from django.contrib.auth.decorators import login_required
from products.models import Product
from django.contrib import messages

# Create your views here.
def remove_item(request,pk):
    item=OrderedItem.objects.get(pk=pk)
    item.delete()
    return redirect('showcart')

def showcart(request):
    user=request.user
    customer=user.customer_profile
    cart_obj,created=Order.objects.get_or_create(owner=customer,order_status=Order.CART_STAGE
                                                 )
    context={'cart':cart_obj}
    return render(request,'cart_container.html',context)

@login_required(login_url='account')
def show_orders(request):
     user=request.user
     customer=user.customer_profile
     #0- Order.CART_STAGE
     all_orders=Order.objects.filter(owner=customer).exclude(order_status=0)
     context={'orders':all_orders}
     return render(request,'order_container.html',context)


def ordered(request):
    if request.POST:
        try:
            user=request.user
            print(user)
            customer=user.customer_profile
            print(customer)
            total=float(request.POST.get('total'))
            print(total)
            order_obj=Order.objects.get(owner=customer,order_status=Order.CART_STAGE)
            if order_obj:
                order_obj.order_status=Order.ORDER_CONFIRMED
                order_obj.total_price=total
                print(type(total))
                print(total)
                order_obj.save()
                
                status_message="your order was created successfully"
                messages.success(request,status_message)
            else:
                messages.error(request,"no item in cart")
        except Exception as e:
                    messages.error(request,e)
        return redirect('showcart')            

@login_required(login_url='account')
def add_to_cart(request):
    if request.POST and request.user.is_authenticated:
        user=request.user
        customer=user.customer_profile
        quantity=request.POST.get('quantity')
        product_id=request.POST.get('product_id')
        cart_obj,created=Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )
        product=Product.objects.get(pk=product_id)
        ordered_item,created=OrderedItem.objects.get_or_create(
            product=product,
            owner=cart_obj)
        if created:
            ordered_item.quantity=quantity
            ordered_item.save()
        else:
            print(type(ordered_item.quantity))
            print(type(quantity))
            ordered_item.quantity=ordered_item.quantity+ int(quantity)
            ordered_item.save()   
        return redirect('showcart')
    else:
         return redirect('account')
   

