
from django.conf import settings
from django.db import models

# Create your models here.

class Programme(models.Model):
    title = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class ProgramState(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


class Module(models.Model):
    title = models.CharField(max_length=510, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class Coordinator(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    UNDISCLOSE = 'U'

    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (UNDISCLOSE, "Don't want to Say"),
    ]

    SUPER_ADMIN = 'S'
    ADMIN = 'A'
    COORDINATOR = 'C'
    INSTRUCTOR = 'I'

    ROLE_CHOICES = [
        (SUPER_ADMIN, 'Super Admin'),
        (ADMIN, 'Admin'),
        (COORDINATOR, "Coordinator"),
        (INSTRUCTOR, "Instructor"),
        
    ]
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=MALE)
    role = models.CharField(max_length=1, choices=ROLE_CHOICES, default=COORDINATOR)
    programstate = models.ManyToManyField(ProgramState)
    programme = models.ManyToManyField(Programme)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)


class Student(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    UNDISCLOSE = 'U'

    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (UNDISCLOSE, "Don't want to Say"),
    ]
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    other_name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=MALE)
    state = models.CharField(max_length=255)
    lga = models.CharField(max_length=255)
    town = models.CharField(max_length=255)
    contact_address = models.TextField()
    qualification = models.CharField(max_length=255, null=True, blank=True)
    occupation = models.CharField(max_length=255, null=True, blank=True)
    identification = models.CharField(max_length=255, null=True, blank=True)
    identification_number = models.CharField(max_length=255, null=True, blank=True)
    programme = models.ForeignKey(Programme, on_delete=models.PROTECT)
    programstate = models.ForeignKey(ProgramState, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    # birth_date = models.DateField(null=True)


class Instructor(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    UNDISCLOSE = 'U'

    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (UNDISCLOSE, "Don't want to Say"),
    ]
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    other_name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=MALE)
    module_handling = models.ManyToManyField(Module)
    # state = models.CharField(max_length=255)
    # lga = models.CharField(max_length=255)
    # town = models.CharField(max_length=255)
    # contact_address = models.TextField()
    # qualification = models.CharField(max_length=255, null=True, blank=True)
    # occupation = models.CharField(max_length=255, null=True, blank=True)
    # identification = models.CharField(max_length=255, null=True, blank=True)
    # identification_number = models.CharField(max_length=255, null=True, blank=True)
    # programme = models.ForeignKey(Programme, on_delete=models.PROTECT)
    # programstate = models.ForeignKey(ProgramState, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    # birth_date = models.DateField(null=True)

    



