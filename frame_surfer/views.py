"""Views for frame_surfer."""

from nautobot.apps.views import NautobotUIViewSet

from frame_surfer import filters, forms, models, tables
from frame_surfer.api import serializers


class FrameSurferFrameTVModelUIViewSet(NautobotUIViewSet):
    """ViewSet for FrameSurferFrameTVModel views."""

    bulk_update_form_class = forms.FrameSurferFrameTVModelBulkEditForm
    filterset_class = filters.FrameSurferFrameTVModelFilterSet
    filterset_form_class = forms.FrameSurferFrameTVModelFilterForm
    form_class = forms.FrameSurferFrameTVModelForm
    lookup_field = "pk"
    queryset = models.FrameTV.objects.all()
    serializer_class = serializers.FrameSurferFrameTVModelSerializer
    table_class = tables.FrameSurferFrameTVModelTable

class FrameSurferUnsplashModelUIViewSet(NautobotUIViewSet):
    """ViewSet for FrameSurferUnsplashModel views."""

    bulk_update_form_class = forms.FrameSurferUnsplashModelBulkEditForm
    filterset_class = filters.FrameSurferUnsplashModelFilterSet
    filterset_form_class = forms.FrameSurferUnsplashModelFilterForm
    form_class = forms.FrameSurferUnsplashModelForm
    lookup_field = "pk"
    queryset = models.UnsplashModel.objects.all()
    serializer_class = serializers.UnsplashModelSerializer
    table_class = tables.FrameSurferUnsplashModelTable

class FrameSurferPhotoModelUIViewSet(NautobotUIViewSet):
    """ViewSet for FrameSurferPhotoModel views."""

    bulk_update_form_class = forms.FrameSurferPhotoModelBulkEditForm
    filterset_class = filters.FrameSurferPhotoModelFilterSet
    filterset_form_class = forms.FrameSurferPhotoModelFilterForm
    form_class = forms.FrameSurferPhotoModelForm
    lookup_field = "pk"
    queryset = models.PhotoModel.objects.all()
    serializer_class = serializers.FrameSurferPhotoModelSerializer
    table_class = tables.FrameSurferPhotoModelTable


# class AddAPIServiceView(NautobotView):
#     template_name = 'frame_surfer/add_api_service.html'
#
#     def get(self, request, *args, **kwargs):
#         form = APIServiceForm()
#         return self.render_to_response({'form': form})
#
#     def post(self, request, *args, **kwargs):
#         form = APIServiceForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('api_service_list'))
#         return self.render_to_response({'form': form})
#
# class APIServiceListView(ObjectListView):
#     queryset = models.UnsplashModel.objects.all()
#     template_name = 'surfer/api_service_list.html'
#     context_object_name = 'api_services'
#
# class AddTVView(NautobotUIViewSet):
#     template_name = 'surfer/add_tv.html'
#
#     def get(self, request, *args, **kwargs):
#         form = TVForm()
#         return self.render_to_response({'form': form})
#
#     def post(self, request, *args, **kwargs):
#         form = TVForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('tv_list'))
#         return self.render_to_response({'form': form})
#
#
# class DownloadPhotoView(NautobotUIViewSet):
#     def post(self, request, tv_id, *args, **kwargs):
#         tv_object = get_object_or_404(FrameTV, id=tv_id)
#         unsplash = UnSplash(tv_object)
#         photo_dir = os.path.join(settings.BASE_DIR, 'photos', tv_object.name)
#
#         if not os.path.exists(photo_dir):
#             os.makedirs(photo_dir)
#
#         unsplash.fetch_random(file_path=photo_dir)
#         return redirect(reverse('tv_list'))
#
# class DownloadedPhotosView(ObjectListView):
#     queryset = models.PhotoModel.objects.all()
#     template_name = 'surfer/downloaded_photos.html'
#     context_object_name = 'photos'