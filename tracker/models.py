from django.db import models

# Create your models here.
from django.contrib.auth.models  import User

class Expense(models.Model):
  CATEGORY=(
    ('Food','Food'),
    ('Travel','Travel'),
    ('Shopping','Shopping'),
    ('Bills','Bills'),
    ('Other','Other'),

  )

  user=models.ForeignKey(User, on_delete=models.CASCADE)
  amount=models.DecimalField(max_digits=10,decimal_places=2)
  category=models.CharField(max_length=20,choices=CATEGORY)
  description=models.CharField(max_length=200)
  date=models.DateField(auto_now_add=True)


  def __str__(self):
    return self.category