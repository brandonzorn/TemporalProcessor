import pyinstaller_versionfile

APP_NAME = "TemporalProcessor"
APP_VERSION = "1.0.1"

pyinstaller_versionfile.create_versionfile(
    output_file="pkg_res/version_info.txt",
    version=APP_VERSION,
    company_name="brandonzorn",
    file_description=f"{APP_NAME}",
    internal_name=APP_NAME,
    legal_copyright="Copyright (c) 2025 brandonzorn",
    original_filename=f"{APP_NAME}.exe",
    product_name=APP_NAME,
)
