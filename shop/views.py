from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Product, Category, Order, OrderItem
from .cart import Cart

# 1. Catálogo de productos (Inicio)
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(stock__gt=0) 

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request, 'shop/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })

# 2. Detalle de un producto individual
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    return render(request, 'shop/product/detail.html', {'product': product})

# 3. Vista del Carrito de compras
def cart_detail(request):
    cart = Cart(request)
    return render(request, 'shop/cart/detail.html', {'cart': cart})

# 4. Añadir producto al carrito
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product, quantity=1)
    return redirect('shop:cart_detail')

# 5. Restar o eliminar producto del carrito
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('shop:cart_detail')

# 6. Crear el pedido 
@login_required 
def order_create(request):
    cart = Cart(request)
    if len(cart) == 0:
        return redirect('shop:product_list')
        
    if request.method == 'POST':
        order = Order.objects.create(
            user=request.user,
            total_amount=cart.get_total_price(),
            status='PAID' 
        )
        
        for item in cart:
            product = item['product']
            OrderItem.objects.create(
                order=order,
                product=product,
                price=item['price'],
                quantity=item['quantity']
            )
            product.stock -= item['quantity']
            product.save()

        cart.clear()
        return render(request, 'shop/order/created.html', {'order': order})
        
    return render(request, 'shop/order/create.html', {'cart': cart})

# 7. Panel de pedidos del usuario logueado
@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'shop/order/list.html', {'orders': orders})

# 8. Vista de Registro para nuevos clientes estilizada
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('shop:product_list')
    else:
        form = UserCreationForm()

        for field in form.fields.values():
            field.widget.attrs.update({'class': 'form-control mb-3'})
            
    return render(request, 'shop/auth/register.html', {'form': form})

# 9. Vista de Inicio de Sesión (Login) 
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(request.GET.get('next', 'shop:product_list'))
    else:
        form = AuthenticationForm()
        
        for field in form.fields.values():
            field.widget.attrs.update({'class': 'form-control mb-3'})
            
    return render(request, 'shop/auth/login.html', {'form': form})

# 10. Vista para cerrar sesión
def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect('shop:product_list')

# 11. Incrementar cantidad (+1) en el carrito
def cart_increment(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product, quantity=1, override_quantity=False)
    return redirect('shop:cart_detail')

# 12. Decrementar cantidad (-1) en el carrito
def cart_decrement(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    
    product_id_str = str(product.id)
    if product_id_str in cart.cart:
        current_quantity = cart.cart[product_id_str]['quantity']
        if current_quantity > 1:
            cart.add(product=product, quantity=current_quantity - 1, override_quantity=True)
        else:
            cart.remove(product)
            
    return redirect('shop:cart_detail')
