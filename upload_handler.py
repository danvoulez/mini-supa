import os
import zipfile
import time

UPLOAD_DIR = 'uploads'

def upload_zip(file_path):
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)
    os.rename(file_path, os.path.join(UPLOAD_DIR, os.path.basename(file_path)))

def unzip_file(file_path):
    retries = 3
    for i in range(retries):
        try:
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(UPLOAD_DIR)
            break
        except Exception as e:
            if i < retries - 1:
                print(f"Error unzipping file: {e}. Retrying ({i+1}/{retries})...")
                time.sleep(10)
            else:
                print(f"Failed to unzip file after {retries} attempts: {e}")
                raise

def delete_zip(file_path):
    try:
        os.remove(file_path)
    except Exception as e:
        print(f"Error deleting zip file: {e}")
        raise
