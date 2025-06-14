# app.py   ──>  run with:  streamlit run app.py
import gzip
import shutil
import tempfile
from pathlib import Path
import streamlit as st

st.title("GZ Extractor (keep original name minus .gz)")

uploaded = st.file_uploader("Upload a .gz file", type=["gz"])

if uploaded:
    # 1️⃣  Save the uploaded bytes to a temporary .gz file
    tmp_gz = tempfile.NamedTemporaryFile(delete=False, suffix=".gz")
    tmp_gz.write(uploaded.read())
    tmp_gz.close()

    # 2️⃣  Build the destination path: same name minus the trailing ".gz"
    orig_name = Path(uploaded.name)          # e.g. file1.sql.gz
    dest_name = orig_name.with_suffix('')    # removes .gz  → file1.sql  OR file2
    dest_path = Path(tmp_gz.name).with_suffix('')  # temp folder, same logic

    # 3️⃣  Decompress
    with gzip.open(tmp_gz.name, 'rb') as fin, open(dest_path, 'wb') as fout:
        shutil.copyfileobj(fin, fout)

    # 4️⃣  Offer the file to download with the correct name
    st.success(f"Extracted → {dest_name}")
    with open(dest_path, 'rb') as f:
        st.download_button(
            "Download unzipped file",
            data=f,
            file_name=dest_name.name,   # ensures user receives file1.sql or file2
        )
