import json
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

def create_qr(request):
    if request.method == "POST":
        data = json.loads(request.body)
        link1 = data.get("link1")
        link2 = data.get("link2")
        print(link1,link2)
        # Store in database
        # qr_entry = QRCodeData.objects.create(link1=link1, link2=link2)
        
        # # Generate QR Code
        # qr_text = f"Link 1: {link1}\nLink 2: {link2}"
        # qr = qrcode.make(qr_text)
        # buffer = BytesIO()
        # qr.save(buffer, format="PNG")
        # qr_image_base64 = base64.b64encode(buffer.getvalue()).decode()
        
        return JsonResponse({"message": "QR Code Created Successfully!"})
    
    return JsonResponse({"error": "Invalid request"}, status=400)


