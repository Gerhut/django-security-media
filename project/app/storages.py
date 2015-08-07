from django.core.files.storage import FileSystemStorage

from django.conf import settings

__all__ = ('security_storage',)

security_storage = FileSystemStorage(
    location=settings.SECURITY_MEDIA_ROOT,
    base_url=settings.SECURITY_MEDIA_URL)
