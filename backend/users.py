from db import db_firestore
from google.cloud.firestore_v1 import FieldFilter

'''
fungsi untuk manajemen user
1. menambahkan user baru
2. mengambil data user berdasarkan id
3. menampilkan semua user
4. update data user
5. delete user
'''

# inisialisasi koneksi database
doc_ref = db_firestore.collection("users")
admins_ref = db_firestore.collection('admins')

def add_user(data):
    '''
    format data request body:
    user = {
        "nama" : "John Doe",
        "email" : "test@email.com",
        "alamat" : "Jl. Contoh No. 123, Jakarta"
        "telepon" : "081234567890"
    }
    '''
    # simpan data ke database
    doc_ref.document().set(data)

    # generate response datanya
    response = {
        "code": 200,
        "message" : "User berhasil di tambahkan",
        "id" : doc_ref.id,
        "data" : data
    }

    return response

# fungsi untuk menampilkan data user
def get_users():
    # stream data user dari database
    user_data = doc_ref.stream()

    data_users = []
    # loop data user
    for user in user_data:
        # looping data user, iterasi satu persatu lalu push ke list data_users
        # data_users.append(user.to_dict())
        # ** kwargs = untuk ambil sisa data lainnya
        data_users.append({"id": user.id, **user.to_dict()})

    # tampilkan semua data users
    response = {
        "code": 200,
        "message" : "User berhasil di tampilkan",
        "data" : data_users
    }

    return response

# fungsi untuk menampilkan data user by id
def get_user_by_id(id):
    user_data = doc_ref.document(id).get()

    if user_data.exists:
        response = {
            "code": 200,
            "message" : "User berhasil di tampilkan",
            "data" : user_data.to_dict()
        }
        return response
    else:
        response = {
            "code": 404,
            "message" : "User tidak ditemukan",
        }
        return response
    

def delete_user(id):
    user_data = get_user_by_id(id)

    if user_data['code'] == 404:
        response = {
            "code": 404,
            "message" : "User tidak ditemukan",
        }
        return response

    
    doc_ref.document(id).delete()

    response = {
        "code": 200,
        "message" : "User berhasil dihapus",
    }
    return response


# update data users
def update_user(id, data):
    user_data = get_user_by_id(id)

    if user_data['code'] == 404:
        response = {
            "code": 404,
            "message" : "User tidak ditemukan",
        }
        return response
    
    '''
    format data request body:
    user = {
        "nama" : "John Doe",
        "email" : "test@email.com",
        "alamat" : "Jl. Contoh No. 123, Jakarta"
        "telepon" : "081234567890"
    }
    '''
    doc_ref.document(id).update(data)

    response = {
        "code": 200,
        "message" : "User berhasil diupdate",
    }
    return response


# fungsi untuk cek apakah user adalah admin
def is_admin(email):
    admin = admins_ref.where(filter=FieldFilter('email', '==', email)).stream()
    return len(list(admin)) > 0


# fungsi untuk mendapatkan semua admin
def get_admins():
    admin_data = admins_ref.stream()
    
    data_admins = []
    for admin in admin_data:
        data_admins.append({"id": admin.id, **admin.to_dict()})
    
    response = {
        "code": 200,
        "message" : "Admin berhasil di tampilkan",
        "data" : data_admins
    }
    
    return response


# fungsi untuk menambahkan admin baru
def add_admin(data):
    '''
    format data request body:
    admin = {
        "nama" : "Admin Name",
        "email" : "admin@email.com"
    }
    '''
    admins_ref.document().set(data)
    
    response = {
        "code": 200,
        "message" : "Admin berhasil di tambahkan",
        "data" : data
    }
    
    return response