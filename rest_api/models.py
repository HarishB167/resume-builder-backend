from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name =  models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    address =  models.TextField()
    profile_statement  = models.TextField()
    profile_link = models.TextField()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Project(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField()
    git_link = models.TextField()
    test_link = models.TextField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE)


class Education(models.Model):
    qualification = models.CharField(max_length=255)
    institute = models.CharField(max_length=255)
    score = models.CharField(max_length=255)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)


class Experience(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    start = models.DateField()
    end = models.DateField()
    responsibilities = models.TextField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    

class Training(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE)


class Skill(models.Model):
    name = models.CharField(max_length=255)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

class Language(models.Model):
    name = models.CharField(max_length=255)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
