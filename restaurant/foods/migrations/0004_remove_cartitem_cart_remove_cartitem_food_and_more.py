# Generated by Django 5.0.2 on 2024-03-30 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0003_cart_cartitem_cart_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='food',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
