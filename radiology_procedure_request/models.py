# Django/DRF imports
from django.db import models

# Local app imports
from hims_api.basemodel import BaseModel
from consultation.models import Consultation
from radiology_procedure.models import RadiologyProcedure
from  diagnosed_procedure.models import Sponsor
from consultation_diagnosis.models import ConsultationDiagnosis
class RadiologyProcedureRequest(BaseModel):

    # consultation_diagnosis = models.ForeignKey(
    #      Consultation,
    #      on_delete=models.PROTECT,
    #      related_name="consultation_radiology_procedure_request",
    #  )
    
    consultation_diagnosis = models.ForeignKey(
         ConsultationDiagnosis,
         on_delete=models.PROTECT,
         related_name="consultation_radiology_procedure_request",null=True
     )
    sponsor = models.ForeignKey (
        Sponsor,
        on_delete=models.CASCADE,
        related_name="rediolo_procedure_sponsor",
        null=True,
        blank=True,
    )

    radiology_procedure = models.ForeignKey(
        RadiologyProcedure,
        on_delete=models.PROTECT,
        related_name="radiology_procedure_radiology_procedure_request",
    )

    price = models.DecimalField(max_digits=5, decimal_places=2)
    
    discount = models.DecimalField(max_digits=5, decimal_places=2)
