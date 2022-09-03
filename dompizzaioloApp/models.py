from django.db import models

# Create your models here.


class User(models.Model):
    cpf_user = models.CharField(max_length=11, null=False)
    name_user = models.CharField(max_length=30, null=False)
    birthDate_user = models.DateField(null=False)
    email = models.EmailField(null=False)
    password_user = models.CharField(max_length=20, null=False)
    password2_user = models.CharField(max_length=20, null=False)
    user_permission = models.BooleanField(default=False)

    def __str__(self):
        return self.name_user


class Food(models.Model):
    name_food = models.CharField(max_length=30, null=False)
    price_food = models.DecimalField(max_digits=5, decimal_places=2)
    image_food = models.ImageField(blank=False)
    food_description = models.TextField(max_length=200, null=False)

    def __str__(self):
        return self.name_food


class Order(models.Model):
    status_flieds = (
        ('S', 'Solicitado'),
        ('P', 'Produção'),
        ('E', 'Entregue')
    )
    name_user = models.ForeignKey(User, on_delete=models.CASCADE)
    name_food = models.ForeignKey(Food, on_delete=models.CASCADE)
    posted = models.BooleanField(default=False)
    status = models.CharField(
        max_length=1, choices=status_flieds, null=False, default='S')
