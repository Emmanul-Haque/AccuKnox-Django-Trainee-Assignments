"""Q3: By default do django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic."""

from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError

# Example model
class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Signal receiver for post_save signal
@receiver(post_save, sender=MyModel)
def my_model_post_save(sender, instance, **kwargs):
    print("Signal handler executing...")
    # Intentionally raise an exception to check transaction rollback
    raise ValidationError("Signal handler exception")

# Function to demonstrate transactional behavior
def create_model_instance():
    try:
        with transaction.atomic():
            print("Saving model instance...")
            instance = MyModel.objects.create(name="Test Instance")
            print("Instance saved!")
    except ValidationError as e:
        print(f"Transaction rolled back due to: {e}")
    
    # Check if the instance was saved to the database
    if MyModel.objects.filter(name="Test Instance").exists():
        print("Instance exists in the database")
    else:
        print("Instance does NOT exist in the database (rollback occurred)")


"""To check the Output
>>> from Django_Q3.models import *
>>> MyModel.objects.all()

>>> create_model_instance()

>>> MyModel.objects.all()   


### Output:
    <QuerySet []>

    Saving model instance...
    Signal handler executing...
    Transaction rolled back due to: ['Signal handler exception']
    Instance does NOT exist in the database (rollback occurred)

    <QuerySet []>
"""