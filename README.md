# mini-supa

## Upload Handler

This repository includes a new upload handler to manage zip files. The upload handler allows you to upload a zip file, unzip it, and delete the zip file.

### How to Use the Upload Handler

1. **Upload a Zip File**

   To upload a zip file, use the `upload_zip` function from the `upload_handler.py` file. This function moves the zip file to the root directory.

   ```python
   from upload_handler import upload_zip

   file_path = 'path/to/your/file.zip'
   upload_zip(file_path)
   ```

2. **Unzip the Uploaded File**

   To unzip the uploaded file, use the `unzip_file` function from the `upload_handler.py` file. This function extracts the contents of the zip file into the root directory.

   ```python
   from upload_handler import unzip_file

   file_path = 'file.zip'
   unzip_file(file_path)
   ```

3. **Delete the Zip File**

   To delete the zip file after extraction, use the `delete_zip` function from the `upload_handler.py` file. This function removes the zip file from the root directory.

   ```python
   from upload_handler import delete_zip

   file_path = 'file.zip'
   delete_zip(file_path)
   ```

### GitHub Action Workflow

A GitHub Action workflow file `unzip-upload.yml` has been added to automate the process of unzipping and deleting uploaded zip files. The workflow triggers on push events, waits for the uploaded zip file, unzips the file, and deletes the zip file. It also includes error handling and retries for the unzip step.

The workflow file is located in the `.github/workflows` directory.
