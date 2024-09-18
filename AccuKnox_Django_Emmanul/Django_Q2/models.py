"""Q2: Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic."""

import threading
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# # Mymodel
class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Signal receiver for post_save signal
@receiver(post_save, sender=MyModel)
def my_model_post_save(sender, instance, **kwargs):
    print(f"Signal Handler Thread ID: {threading.get_ident()} - Instance: {instance.name}")


"""To check the Output
>>> from Django_Q2.models import MyModel
>>> import threading                    
>>> print(f"Caller Thread ID: {threading.get_ident()}")

>>> instance = MyModel.objects.create(name="Md. Emmanul Haque")

### Output:
    Caller Thread ID: 1672
    Signal Handler Thread ID: 1672 - Instance: Md. Emmanul Haque
    NOTE: This is the second time I am checking the output before final submission. Therfore, this output may vary from that in the PDF file.
"""