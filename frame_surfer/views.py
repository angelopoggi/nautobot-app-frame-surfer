"""Views for frame_surfer."""

from nautobot.apps.views import NautobotUIViewSet

from frame_surfer import filters, forms, models, tables
from frame_surfer.api import serializers


class FrameSurferExampleModelUIViewSet(NautobotUIViewSet):
    """ViewSet for FrameSurferExampleModel views."""

    bulk_update_form_class = forms.FrameSurferExampleModelBulkEditForm
    filterset_class = filters.FrameSurferExampleModelFilterSet
    filterset_form_class = forms.FrameSurferExampleModelFilterForm
    form_class = forms.FrameSurferExampleModelForm
    lookup_field = "pk"
    queryset = models.FrameSurferExampleModel.objects.all()
    serializer_class = serializers.FrameSurferExampleModelSerializer
    table_class = tables.FrameSurferExampleModelTable
