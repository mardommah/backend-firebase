from backend.account import handler_register, handler_login

data = {
    "username": "test",
    "email": "test2@email.com",
    "password": "test123",
    "confirm_password": "test123"
}

# print(handler_register(data['username'], data['email'], data['password'], data['confirm_password']))

print(handler_login(data['email'], data['password']))