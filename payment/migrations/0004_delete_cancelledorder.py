# Generated by Django 5.0.6 on 2024-07-09 10:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("payment", "0003_alter_orderitem_order_cancelledorder"),
    ]

    operations = [
        migrations.DeleteModel(
            name="CancelledOrder",
        ),
    ]
