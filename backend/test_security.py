from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)

password = "admin123"

hashed = hash_password(password=password)

print("Hashed Password:")
print(hashed)

print()

print("Password Match:")
print(verify_password(password=password, hashed_password=hashed))

print()

token = create_access_token(
    {
        "sub": "sumit@gmal.com"
    }
)

print("JWT token")
print(token)