import inspect
import os
import shutil
import time


def get_func_patch_name(f):
    if inspect.isfunction(f):
        return f"{f.__module__}.{f.__name__}"
    if inspect.ismethod(f):
        return f"{f.__module__}.{f.__self__.__class__.__name__}.{f.__name__}"
    if inspect.isclass(f):
        return f"{f.__module__}.{f.__name__}"
    return "unknown_name"


def delete_old_image(old_image):
    if old_image:
        print(f"🗑️ Deleting from storage: {old_image.name}")
        old_image.delete(save=False)
    else:
        print("🗑️ File not found...")


def delete_attachments_by_product_id(folder_path):
    if os.path.exists(folder_path):
        if os.path.isdir(folder_path):
            shutil.rmtree(folder_path)
        print("Folder deleted successfully")

