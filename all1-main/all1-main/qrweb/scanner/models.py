from django.db import models

class QRCode(models.Model):
    link1 = models.URLField()
    link2 = models.URLField()
    qr_code_path = models.CharField(max_length=255)  # Store file path of the QR image
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"QR for {self.link1} & {self.link2}"
