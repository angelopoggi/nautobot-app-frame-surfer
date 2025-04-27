"""Django urlpatterns declaration for frame_surfer app."""

from django.templatetags.static import static
from django.urls import path
from django.views.generic import RedirectView
from nautobot.apps.urls import NautobotUIViewSetRouter


from frame_surfer import views


app_name = "frame_surfer"
router = NautobotUIViewSetRouter()

# The standard is for the route to be the hyphenated version of the model class name plural.
# for example, ExampleModel would be example-models.
router.register("frame-surfer-example-models", views.FrameSurferExampleModelUIViewSet)


urlpatterns = [
    path("docs/", RedirectView.as_view(url=static("frame_surfer/docs/index.html")), name="docs"),
]

urlpatterns += router.urls
