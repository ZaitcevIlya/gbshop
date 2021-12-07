from django.db import models
# from django.conf import settings

from users.models import User
from mainapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='product quantity', default=0)
    add_datetime = models.DateField(verbose_name='added on', auto_now_add=True)


