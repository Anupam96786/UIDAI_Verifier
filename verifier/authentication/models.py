from django.db import models


class EKYC(models.Model):
    """
    EKYC model
    """
    id = models.AutoField(primary_key=True)
    eKycXML = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.created_at)
