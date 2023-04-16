from django.shortcuts import render

from .form import signUpForm
from . models import *
from django.http import JsonResponse
from django.shortcuts import render, redirect
import json
import datetime
from django.contrib.auth.forms import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.



def loginpage(request):
    page = "login"
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "user does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "password does not exist")

    if User.is_authenticated:
        username = request.user.username
    else:
        username == 'Username'

    context = {'page': page, "username": username}
    return render(request, 'login.html', context)



def logoutUser(request):
    logout(request)
    return redirect('home')

def registerpage(request):
    form = signUpForm()
    if request.method == "POST":
       form = signUpForm(request.POST)
       if form.is_valid():
            user = form.save(commit=False)
            user.email= user.email.lower()
            user.save()
            login(request, user)
            return redirect("home")
       else:
           messages.error(request, "an error occurred during registration")

    context = {'form':form}
    return render(request,'login.html', context)


def home(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        get_orderitems = order.orderitem_set.all().count()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
        get_orderitems = 0

    q = request.GET.get('q') if request.GET.get('q') != None else ''
    products = Product.objects.filter(
        Q(product_type__name__icontains=q)
    )
    context = {"products": products, 'cartItems': cartItems, 'get_orderitems':get_orderitems }
    return render(request, 'index.html', context)

def cars(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        get_orderitems = order.orderitem_set.all().count()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
        get_orderitems = 0


        products = Product.objects.filter(
        Q(product_type__name__icontains='car')
        )
    context = {"products": products, 'cartItems': cartItems, 'get_orderitems':get_orderitems }
    return render(request, 'cars.html', context)

def blog(request):

    context = {}
    return render(request, 'blog.html', context)


def blogDetails(request):

    context = {}
    return render(request, 'blog-details.html', context)

@login_required(login_url='login')
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        get_orderitems = order.orderitem_set.all().count()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
        get_orderitems = 0
    context = {"items": items, "order": order, "cartItems": cartItems, 'get_orderitems':get_orderitems }
    return render(request, 'checkout.html', context)

def clothing(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        get_orderitems = order.orderitem_set.all().count()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
        get_orderitems = 0

    products = Product.objects.filter(
        Q(product_type__name__icontains='cloth')
    )
    context = {"products": products, 'cartItems': cartItems, 'get_orderitems':get_orderitems }
    return render(request, 'clothing.html', context)

def contact(request):

    context = {}
    return render(request, 'contact.html', context)

def furnitures(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        get_orderitems = order.orderitem_set.all().count()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
        get_orderitems = 0

    products = Product.objects.filter(
        Q(product_type__name__icontains='furniture')
    )
    context = {"products": products, 'cartItems': cartItems,'get_orderitems':get_orderitems }
    return render(request, 'furnitures.html', context)


def products(request):

    context = {}
    return render(request, 'products.html', context)

def realestate(request):


    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        get_orderitems = order.orderitem_set.all().count()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
        get_orderitems = 0


    products = Product.objects.filter(
        Q(product_type__name__icontains='hous')
    )
    context = {"products": products, 'cartItems': cartItems,'get_orderitems':get_orderitems}
    return render(request, 'realestate.html', context)

def shopdetails(request, pk):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        get_orderitems = order.orderitem_set.all().count()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
        get_orderitems=0

    menu = Product.objects.get(id=pk)

    products = Product.objects.filter(
        Q(product_type__name__icontains= menu.product_type.name)
    )
    context = {'menu': menu, 'cartItems': cartItems, 'products':products , 'get_orderitems':get_orderitems}
    return render(request, 'shop-details.html', context)

def shopGrid(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        get_orderitems = order.orderitem_set.all().count()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
        get_orderitems = 0

    q = request.GET.get('q') if request.GET.get('q') != None else ''
    products = Product.objects.filter(
        Q(product_type__name__icontains=q)
    )
    context = {"products": products, 'cartItems': cartItems,'get_orderitems':get_orderitems}
    return render(request, 'shop-grid.html', context)

def shopingCart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        get_orderitems = order.orderitem_set.all().count()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
        get_orderitems = 0

    context = {"items": items, "order": order, 'cartItems': cartItems,'get_orderitems':get_orderitems}
    return render(request, 'shoping-cart.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    cartItems = order.get_cart_items
    Customer_order = OrderItem.objects.filter(order__customer=customer, order__complete=False)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == "remove":
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()


    cartItems = order.get_cart_items
    data = []
    for obj in Customer_order:
        item = {
            'id': obj.product.id,
            'product':obj.product.name,
            'quantity':obj.quantity,
            'image': obj.product.image.url,
            'get_total': obj.get_total,
            'price': obj.product.price,



        }
        data.append(item)
    get_cart_total= obj.order.get_cart_total
    return JsonResponse({"data": data,"get_cart_total":get_cart_total,"cartItems":cartItems })

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created =Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])

        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete =True
        order.save()

        Delivery.objects.create(
            customer=customer,
            order=order,
            first_name=data['form']['first_name'],
            last_name=data['form']['last_name'],
            address=data['form']['address'],
            apartment=data['form']['apartment'],
            country=data['form']['country'],
            city=data['form']['city'],
            state=data['form']['state'],
            post_code=data['form']['Postcode'],
            email=data['form']['email'],
            order_note=data['form']['notes'],
            phone_number=data['form']['phone'],
            total=data['form']['total'],

        )

    else:
        print('User is not logged in...')
    return JsonResponse('payment is complete!', safe=False)