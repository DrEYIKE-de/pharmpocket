from django.db import models
import uuid



class ModelsUtils (models.Model):
    pkid = models.BigAutoField(primary_key=True, editable= False, unique= True,)
    id = models.UUIDField(default=uuid.uuid4, unique=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    class Meta:
        abstract = True