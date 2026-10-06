from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    slug = models.SlugField(unique=True, max_length=100)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="Categoría")
    name = models.CharField(max_length=200, verbose_name="Nombre")
    slug = models.SlugField(unique=True, max_length=200)
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="Imagen")
    description = models.TextField(blank=True, verbose_name="Descripción")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    stock = models.IntegerField(default=0, verbose_name="Inventario")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pendiente'),
        ('PAID', 'Pagado'),
        ('SHIPPED', 'Enviado'),
        ('CANCELLED', 'Cancelado'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', verbose_name="Usuario")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING', verbose_name="Estado")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Monto Total")

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

    def __str__(self):
        return f"Pedido {self.id} - {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name="Pedido")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, verbose_name="Producto")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio Unitario")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Cantidad")

    def __str__(self):
        return f"{self.quantity} x {self.product.name if self.product else 'Producto Eliminado'}"
