# tambahkan package untuk akses fitur firebase
import os
import json
import base64
import firebase_admin
from firebase_admin import credentials, firestore

#buatkan koneksi ke database firestore
creds_env = os.environ.get('FIREBASE_CREDENTIALS')
if creds_env:
    # Vercel: baca dari environment variable (base64 encoded)
    creds_dict = json.loads(base64.b64decode(creds_env))
    creds = credentials.Certificate(creds_dict)
else:
    # Lokal: baca dari file
    creds = credentials.Certificate('creds.json')

firebase_admin.initialize_app(creds)

# buat variabel untuk akses database

db_firestore = firestore.client()
print("koneksi database berhasil")