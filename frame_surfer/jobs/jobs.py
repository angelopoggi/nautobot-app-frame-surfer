from nautobot.apps.jobs import Job, register_jobs, ObjectVar
from openid.extensions.sreg import data_fields

#from frame_surfer.api_utils import UnSplash
from frame_surfer.models import UnsplashModel, PhotoModel, FrameTV
from PIL import Image
import requests
import datetime
from urllib.parse import urlparse, urlunparse, quote

class FetchRandomJob(Job):
    """
    A job that fetches a random item from a predefined list.
    """
    class Meta:
        name = "Fetch Random"
        description = "A job that fetches a random photo from unsplash based on the given parameters."

    unsplash = ObjectVar(
        model=UnsplashModel,
        description="Pick the Unsplash Service to use",
        required=True,
    )
    tv = ObjectVar(
        model=FrameTV,
        description="Pick the Frame TV to use",
        required=True,
    )
    def _resize_image(self, image_path):
        # Open the image
        img = Image.open(image_path)

        # Calculate the target aspect ratio dimensions for 16:9
        original_width, original_height = img.size
        target_width = original_width
        target_height = int(target_width * (9 / 16))

        # Check if the new height is larger than the original height
        if target_height > original_height:
            # Scale down width to fit the original height
            target_height = original_height
            target_width = int(target_height * (16 / 9))

        # Calculate cropping area to maintain center
        left = (original_width - target_width) // 2
        top = (original_height - target_height) // 2
        right = left + target_width
        bottom = top + target_height

        # Crop the image to maintain a 16:9 aspect ratio
        cropped_img = img.crop((left, top, right, bottom))

        # Resize the image to the specified dimensions (3840x2160)
        resized_img = cropped_img.resize((3830, 2100))

        # Save the image
        resized_img.save(image_path)

    def _normalize_url(self, raw_url):
        parsed = urlparse(raw_url.strip(), scheme="https")
        if not parsed.netloc:
            parsed = parsed._replace(netloc=parsed.path, path="")
        path = quote(parsed.path)
        return urlunparse(parsed._replace(path=path))

    def run(self, *, unsplash,tv, **kwargs):
        """Run the job."""
        #Step 1 Download a Photo from Unsplash
        #Fix this to be dynamic later
        url = 'https://api.unsplash.com/photos/random/?w=3840&h=2160&topics=WdChqlsJN9c,6sMVjTLSkeQ&content_filter=high&orientation=landscape'
        header = {
            "Authorization": f"Client-ID {unsplash.oauth_token}"
        }
        response = requests.get(url,
                                headers=header,
                                )
        if response.status_code != 200:
            self.log_failure(f"Failed to fetch photo: {response.status_code} - {response.text}")
            return
        data = response.json()
        with requests.get(data['links']['download'], stream=True) as download_response:
                # save information about the photo to the database
                normalized_url = self._normalize_url(data['urls']['raw'])
                photo = PhotoModel.objects.create(
                    name=data['id'],
                    downloaded_at=datetime.datetime.now(),
                    url=normalized_url,
                    tv=tv,
                )
                photo.validated_save()
                #save to local file system
                content = b"".join(download_response.iter_content(1024))
                self.create_file("{data['id']}.jpg", content)


jobs = [FetchRandomJob]
register_jobs(*jobs)