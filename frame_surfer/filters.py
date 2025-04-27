"""Filtering for frame_surfer."""

from nautobot.apps.filters import NameSearchFilterSet, NautobotFilterSet

from frame_surfer import models


class FrameSurferExampleModelFilterSet(NameSearchFilterSet, NautobotFilterSet):  # pylint: disable=too-many-ancestors
    """Filter for FrameSurferExampleModel."""

    class Meta:
        """Meta attributes for filter."""

        model = models.FrameSurferExampleModel

        # add any fields from the model that you would like to filter your searches by using those
        fields = "__all__"
