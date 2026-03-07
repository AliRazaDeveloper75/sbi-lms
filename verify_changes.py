import os
import django
from django.conf import settings
from django.contrib.auth import get_user_model
from accounts.utils import generate_password

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

def test_password_policy():
    print("Testing password policy...")
    User = get_user_model()
    try:
        # Check if validators are empty
        validators = settings.AUTH_PASSWORD_VALIDATORS
        print(f"AUTH_PASSWORD_VALIDATORS: {validators}")
        if len(validators) == 0:
            print("[SUCCESS] Password validators are empty.")
        else:
            print("[FAILURE] Password validators are NOT empty.")

        # Test simple password generation
        pwd = generate_password()
        print(f"Generated password: {pwd}")
        if len(pwd) == 8 and pwd.islower():
            print("[SUCCESS] Simplified password generated.")
        else:
            print("[FAILURE] Password generation not simplified.")

    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    test_password_policy()
