from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Task


@receiver(pre_save, sender=Task)
def batch_manager(sender, instance, *args, **kwargs):
    # batch = Batch.objects.filter(batch = datetime.date.today()).first()
    # if not batch:
    #     batch =  Batch.objects.create(batch = datetime.date.today())
    #     instance.batch_batch.save()

    pass
