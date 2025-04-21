import os
import zipfile

root_dir = 'D:\Final Thesis\Data\MVF\Action Spoting'  # Adjust this to your D drive path if needed

def unzip_files(zip_filepath, extract_dir):
    """Unzips the contents of a zip file to the specified directory."""
    try:
        with zipfile.ZipFile(zip_filepath, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)
        print(f"Successfully unzipped '{os.path.basename(zip_filepath)}' to '{extract_dir}'")
        os.remove(zip_filepath)
        print(f"Deleted '{os.path.basename(zip_filepath)}'")

    except zipfile.BadZipFile:
        print(f"Error: '{zip_filepath}' is not a valid zip file.")
    except Exception as e:
        print(f"An error occurred while unzipping '{zip_filepath}': {e}")

def process_folders(parent_dir):
    """Recursively processes folders to find and unzip zip files in grandchild folders."""
    for item in os.listdir(parent_dir):
        item_path = os.path.join(parent_dir, item)
        if os.path.isdir(item_path):
            # Check if this is a child folder (one level down from D:\)
            for grandchild_item in os.listdir(item_path):
                grandchild_path = os.path.join(item_path, grandchild_item)
                if os.path.isdir(grandchild_path):
                    # This is a grandchild folder, look for zip files
                    for filename in os.listdir(grandchild_path):
                        if filename.endswith(".zip"):
                            zip_file_path = os.path.join(grandchild_path, filename)
                            extract_folder_name = filename[:-4]  # Remove the .zip extension
                            extract_path = os.path.join(grandchild_path, extract_folder_name)
                            os.makedirs(extract_path, exist_ok=True)
                            unzip_files(zip_file_path, extract_path)
            # Recursively process subfolders in case of deeper nesting (though not specified)
            process_folders(item_path)


if __name__ == "__main__":
    print(f"Starting to scan folders in '{root_dir}' for zip files...")
    process_folders(root_dir)
    print("Finished scanning and unzipping.")