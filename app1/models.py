from django.db import models

# Create your models here.
class Department(models.Model):
    title = models.CharField(verbose_name="Department Name", max_length=100)

    def __str__(self):
        return self.title

class User(models.Model):
    username = models.CharField(verbose_name="Username", max_length=100)
    password = models.CharField(verbose_name="Password", max_length=100)
    email = models.EmailField(verbose_name="Email", max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    gender_selection = ((1, "Male"), (2, "Female"), (3, "Unknown"))
    gender = models.SmallIntegerField(verbose_name="Gender", choices=gender_selection)
    dob = models.DateField(verbose_name="Date of Birth", blank=True, null=True)

class PrettyNum(models.Model):
    mobile = models.CharField(verbose_name="mobile", max_length=10)
    price = models.FloatField(verbose_name="price")
    level_choice = {
        (1, "Normal Member"),
        (2, "Sliver Member"),
        (3, "Golden Member"),
        (4, "Primer Member ")
    }
    level = models.SmallIntegerField(verbose_name="level", choices=level_choice)
    state_choice = ((1, "Used"), (2, "Not Used"))
    state = models.SmallIntegerField(verbose_name="State", choices=state_choice)