"""Forms for frame_surfer."""

from django import forms
from nautobot.apps.forms import NautobotBulkEditForm, NautobotFilterForm, NautobotModelForm, TagsBulkEditFormMixin

from frame_surfer import models


class FrameSurferExampleModelForm(NautobotModelForm):  # pylint: disable=too-many-ancestors
    """FrameSurferExampleModel creation/edit form."""

    class Meta:
        """Meta attributes."""

        model = models.FrameSurferExampleModel
        fields = "__all__"


class FrameSurferExampleModelBulkEditForm(TagsBulkEditFormMixin, NautobotBulkEditForm):  # pylint: disable=too-many-ancestors
    """FrameSurferExampleModel bulk edit form."""

    pk = forms.ModelMultipleChoiceField(queryset=models.FrameSurferExampleModel.objects.all(), widget=forms.MultipleHiddenInput)
    description = forms.CharField(required=False)

    class Meta:
        """Meta attributes."""

        nullable_fields = [
            "description",
        ]


class FrameSurferExampleModelFilterForm(NautobotFilterForm):
    """Filter form to filter searches."""

    model = models.FrameSurferExampleModel
    field_order = ["q", "name"]

    q = forms.CharField(
        required=False,
        label="Search",
        help_text="Search within Name.",
    )
    name = forms.CharField(required=False, label="Name")
