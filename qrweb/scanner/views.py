import cv2
import numpy as np
import base64
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import qrcode
import os
from django.conf import settings
@csrf_exempt
def qr_scanner(request):
    """Renders the QR scanner page."""
    return render(request, "qr_scanner.html")

@csrf_exempt
def qr_redirect(request):
    """Handles QR code scanning and redirects accordingly."""
    
    if request.method == "POST":
        data_url = request.POST.get("image")
        source = request.POST.get("source", "unknown")

        if not data_url:
            return JsonResponse({"status": "error", "message": "No image data received."})

        try:
            if "," in data_url:
                _, encoded = data_url.split(",", 1)
            else:
                return JsonResponse({"status": "error", "message": "Invalid image format."})

            image_data = base64.b64decode(encoded)
            np_arr = np.frombuffer(image_data, np.uint8)

            if np_arr.size == 0:
                return JsonResponse({"status": "error", "message": "Decoded image is empty."})

            frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

            if frame is None:
                return JsonResponse({"status": "error", "message": "Failed to decode image."})

            # QR Code Detection
            qr_detector = cv2.QRCodeDetector()
            decoded_data, points, _ = qr_detector.detectAndDecode(frame)

            if decoded_data:
                print(f"Scanned QR Code URL: {decoded_data}")
                print(f"Source: {source}")

                # Redirect logic
                if source == "qr_app":
                    return JsonResponse({"status": "success", "url": "https://www.chatgpt.com"})  # ✅ Fixed URL
                else:
                    return JsonResponse({"status": "success", "url": "https://google.com"})

            else:
                return JsonResponse({"status": "no_qr", "message": "No QR Code detected."})

        except Exception as e:
            return JsonResponse({"status": "error", "message": f"Exception: {str(e)}"})

    return JsonResponse({"status": "error", "message": "Invalid request method."})

import os
import qrcode
from django.conf import settings
from django.http import JsonResponse

def create_qr(request):
    """Generates and saves a QR code dynamically based on user input."""

    # Get links from request parameters
    link1 = request.POST.get("link1", "")
    link2 = request.POST.get("link2", "")

    if not link1 or not link2:
        return JsonResponse({"error": "Missing links"}, status=400)

    # Encode links into a redirect URL
    redirect_url = f"http://127.0.0.1:8000/qr_redirect?link1={link1}&link2={link2}"
    
    # Generate QR code
    qr = qrcode.make(redirect_url)

    # Define the STATIC path for saving the QR code
    qr_directory = os.path.join(settings.STATICFILES_DIRS[0], "image")

    # Ensure the directory exists
    os.makedirs(qr_directory, exist_ok=True)

    # Save the QR code image
    qr_filename = "qr_code2.png"
    qr_path = os.path.join(qr_directory, qr_filename)
    qr.save(qr_path)

    # Return the QR static URL
    return JsonResponse({"qr_path": f"/static/image/{qr_filename}"})

def display_qr(request):
    return render(request, "display_qr.html")


