from django.db import models

# Create your models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

def __str__(self):
    return f"Order {self.id} - {self.customer.name}"

#The Customer model has name and email fields.
#The Order model has a foreign key linking it to the Customer model, using on_delete=models.CASCADE to ensure orders are deleted if the associated customer is removed.