"""API serializers for frame_surfer."""

from nautobot.apps.api import NautobotModelSerializer, TaggedModelSerializerMixin

from frame_surfer import models


class FrameSurferExampleModelSerializer(NautobotModelSerializer, TaggedModelSerializerMixin):  # pylint: disable=too-many-ancestors
    """FrameSurferExampleModel Serializer."""

    class Meta:
        """Meta attributes."""

        model = models.FrameSurferExampleModel
        fields = "__all__"

        # Option for disabling write for certain fields:
        # read_only_fields = []
