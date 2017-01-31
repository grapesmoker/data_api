from tastypie.resources import ModelResource
from hmda.models import LoanApplicationRecord, Institution


class LARResource(ModelResource):

    class Meta:
        queryset = LoanApplicationRecord.objects.all()
        resource_name = 'lar'
        limit = 0


class InstitutionResource(ModelResource):

    class Meta:
        queryset = Institution.objects.all()
        resource_name = 'institution'
        limit = 0