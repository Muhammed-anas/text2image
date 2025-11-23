from django.shortcuts import render
from django.conf import settings
import requests
import os
import uuid

def generate_image(request):
    image_url = None
    error = None

    if request.method == "POST":
        prompt = request.POST.get("prompt")

        if not prompt:
            error = "Please enter a prompt."
        else:
            try:
                url = f"https://image.pollinations.ai/prompt/{requests.utils.quote(prompt)}"
                response = requests.get(url, timeout=20)

                if response.status_code == 200:
                    gallery_path = os.path.join(settings.BASE_DIR, "text2image", "static", "gallery")
                    os.makedirs(gallery_path, exist_ok=True)

                    filename = f"{uuid.uuid4().hex[:8]}.png"
                    file_path = os.path.join(gallery_path, filename)

                    with open(file_path, "wb") as img:
                        img.write(response.content)

                    image_url = f"/static/gallery/{filename}"
                else:
                    error = "Unable to generate image. Please try again."

            except Exception:
                error = "Something went wrong. Try again."

    return render(request, "index.html", {
        "image_url": image_url,
        "error": error
    })
