from django.test import TestCase

# Create your tests here.

from models import StudentSubject
qs = StudentSubject.objects.all()
print(qs)