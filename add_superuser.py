from django.contrib.auth.models import User

user_name = 'admin'
email = 'email@example.com'
password = '12345678a'

if not User.objects.filter(username=user_name).exists():
    User.objects.create_superuser(user_name, email, password)

print("super user created !!!. login with following credentials")
print(user_name)
print(email)
print(password)
