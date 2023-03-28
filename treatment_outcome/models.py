from django.db import models
from patient_discharge.models import PatientDischarge
from  hims_api.basemodel import BaseModel
# Create your models here.

class TreatmentOutcome(BaseModel):
    discharged = models.BooleanField(default=True)
    died = models.BooleanField(default=False)
    cout = models.CharField(max_length=200,blank=True,null=True)
    absconded = models.BooleanField(default=False,help_text="Discharged against medical advice")
    patient_discharge = models.ForeignKey(PatientDischarge,on_delete=models.PROTECT,related_name='patients_discharge',help_text="patients discharge id")

    def __str__(self):
        return  "{} {}".format(self.discharged,self.Patient_discharge)



