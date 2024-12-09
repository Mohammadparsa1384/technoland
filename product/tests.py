from django.test import TestCase

# Create your tests here.
def sep_email(email):
    return email.split("@")[0]

print(sep_email("parsa@gmail.com"))