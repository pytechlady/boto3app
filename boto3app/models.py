# from django.db import models
# import uuid

# # Create your models here.
# class MerchantImage(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     business_name = models.CharField(max_length=255)
#     business_description = models.TextField()
#     cover_image = models.FileField(upload_to='media/')
#     profile_image = models.FileField(upload_to='media/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)