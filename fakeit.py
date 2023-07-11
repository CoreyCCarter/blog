import csv
from faker import Faker

fake = Faker()

with open('users.csv', 'w', newline='') as file:
    fieldnames = ['username', 'email', 'password']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    for _ in range(10):
        username = fake.user_name()
        email = fake.email()
        password = fake.password()

        writer.writerow({'username': username, 'email': email, 'password': password})

print('Users generated and saved successfully.')