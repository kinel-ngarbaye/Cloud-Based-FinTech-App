import firebase_admin
from firebase_admin import credentials, auth

# Initialize Firebase Admin SDK
cred = credentials.Certificate("path/to/your/firebase-adminsdk.json")
firebase_admin.initialize_app(cred)

# Example: Create new user
def create_user(email, password):
    user = auth.create_user(
        email=email,
        password=password
    )
    print(f'Successfully created new user: {user.uid}')

# Example: Verify user ID token
def verify_user_token(id_token):
    try:
        decoded_token = auth.verify_id_token(id_token)
        uid = decoded_token['uid']
        print(f'User ID: {uid}')
        return uid
    except Exception as e:
        print(f"Error verifying token: {e}")
