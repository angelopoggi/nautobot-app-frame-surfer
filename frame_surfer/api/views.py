"""API views for frame_surfer."""

from nautobot.apps.api import NautobotModelViewSet

from frame_surfer import filters, models
from frame_surfer.api import serializers


class FrameSurferExampleModelViewSet(NautobotModelViewSet):  # pylint: disable=too-many-ancestors
    """FrameSurferExampleModel viewset."""

    queryset = models.FrameSurferExampleModel.objects.all()
    serializer_class = serializers.FrameSurferExampleModelSerializer
    filterset_class = filters.FrameSurferExampleModelFilterSet

    # Option for modifying the default HTTP methods:
    # http_method_names = ["get", "post", "put", "patch", "delete", "head", "options", "trace"]
