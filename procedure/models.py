from django.db import models
from choice.views import StatusChoice
from django.contrib.auth.models import User

from status.models import Status

class ProcedureType(models.Model):
    name = models.CharField(max_length=100,null=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="procedure_type_user"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Procedure(models.Model):
    name = models.TextField(max_length=100, null=False, unique=True)
    procedure_type = models.ForeignKey(ProcedureType,on_delete=models.PROTECT,null=True,related_name="procedure_types")
    description = models.TextField(max_length=100, null=True, blank=True, unique=False)
    gdrg = models.TextField(max_length=200, null=True, blank=True, unique=False)
    icd_code = models.TextField(max_length=100, null=True, blank=True, unique=False)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="procedure_user"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(
        Status, on_delete=models.CASCADE, related_name="procedure_user"
    )

    def __str__(self):
        return "{}".format(self.name)
