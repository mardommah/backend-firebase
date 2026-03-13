# tambahkan package untuk akses fitur firebase
import firebase_admin
from firebase_admin import credentials, firestore

#buatkan koneksi ke database firestore
creds = credentials.Certificate('creds.json')
firebase_admin.initialize_app(creds)

# buat variabel untuk akses database

db_firestore = firestore.client()
print("koneksi database berhasil")