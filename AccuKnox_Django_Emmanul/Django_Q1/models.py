"""Q1: By default, are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic."""

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Example model with a signal
class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Signal definition and receiver
@receiver(post_save, sender=MyModel)
def my_model_post_save(sender, instance, created, **kwargs):
    print(f"Signal received for instance {instance}")


"""To check the Output
>>> from Django_Q1.models import MyModel
>>> instance = MyModel.objects.create(name="Md. Emmanul Haque")

### Output:
    Signal received for instance MyModel object (1)
"""