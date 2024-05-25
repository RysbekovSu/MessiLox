from django.db import models

# Create your models here.
# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Sum, F


class CustomUser(AbstractUser):
    # profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    passport_id = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(
        max_length=100,
        choices=[
            ('Waiter', 'Waiter'),
            ('Chef', 'Chef'),
            ('Admin', 'Admin'),
        ],
        blank=True,
        null=True
    )
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name}+{self.username}"


class Table(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True, null=False)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    image = models.ImageField(upload_to='food_images/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    # category = models.ForeignKey('Category', on_delete=models.P   ROTECT, null=True)
    # user = models.ForeignKey(CustomUser,default=1, verbose_name='USer', on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category,
        to_field='name',
        on_delete=models.PROTECT,
        db_column='category_name',
        null=True
    )

    def __str__(self):
        return self.name


class Book(models.Model):
    time = models.DateTimeField()
    # table = models.ForeignKey(Table, on_delete=models.CASCADE)

    table = models.ForeignKey(
        Table,
        to_field='name',
        on_delete=models.PROTECT,
        db_column='table_name',
        null=True
    )

    deposit = models.DecimalField(max_digits=10, decimal_places=2)
    customer_name = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Booking at {self.time} for table {self.table.name}"


class Order(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)

    # employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    employee = models.ForeignKey(
        CustomUser,
        to_field='username',
        on_delete=models.PROTECT,
        db_column='employee_username',
        null=True

    )

    def __str__(self):
        return f"Order {self.id} by {self.employee.get_full_name()}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    # food = models.ForeignKey(Food, on_delete=models.CASCADE)

    food = models.ForeignKey(
        Food,
        to_field='name',
        on_delete=models.PROTECT,
        db_column='food_name',
        null=True

    )
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.food.name} for order {self.order.id}"


class Payment(models.Model):
    payed_status = models.BooleanField(default=False)
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    total_sum = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def calculate_total_sum(self):
        total = OrderItem.objects.filter(order=self.order).aggregate(
            total=Sum(F('quantity') * F('food__price'))
        )['total']
        return total if total is not None else 0.00

    def save(self, *args, **kwargs):
        self.total_sum = self.calculate_total_sum()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Payment for order {self.order.id} - {'Paid' if self.payed_status else 'Unpaid'}"
