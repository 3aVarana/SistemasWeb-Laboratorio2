from tastypie.resources import ModelResource
from .models import Patient
from tastypie.authorization import Authorization

class PatiensResource(ModelResource):
    class Meta:
        queryset = Patient.objects.all()
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'patient'
        authorization = Authorization()

