from django.utils.safestring import mark_safe
from django.core.files.storage import get_storage_class


# Displays image to Admin Panel as Image Tags
def ImageTag(image):
    return mark_safe('<img src="/../../media/%s" width="50" height="50" />' % (image))


# Overwrites a file if it is already present with the given name
class OverwriteStorage(get_storage_class()):
    
    def _save(self, name, content):
        self.delete(name)
        return super(OverwriteStorage, self)._save(name, content)

    def get_available_name(self, name, max_length=None):
        return name