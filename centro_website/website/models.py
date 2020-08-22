from django.db import models
from django.utils import timezone

class User(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    SEX_OPTIONS = [
        (MALE, 'Masculino'),
        (FEMALE, 'Femenino'),
    ]
    ADMINISTRATOR = 'AD'
    THERAPIST = 'TR'
    REPRESENTATIVE = 'RP'
    ROL_OPTIONS = [
        (ADMINISTRATOR, 'Administrador'),
        (THERAPIST, 'Terapeuta'),
        (REPRESENTATIVE, 'Representante'),
    ]
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    identity_card = models.CharField(max_length=10)
    registration_date = models.DateTimeField(auto_now_add=True)
    rol = models.CharField(max_length=2, choices=ROL_OPTIONS, default=REPRESENTATIVE)
    birth = models.DateField()
    sex = models.CharField(max_length=1, choices=SEX_OPTIONS, default=MALE)
    civil_status = models.CharField(max_length=150)
    phone_number_1 = models.PositiveIntegerField()
    phone_number_2 = models.PositiveIntegerField()
    email = models.EmailField(max_length=250, null=True)
    direction = models.ForeignKey('Direction', on_delete=models.DO_NOTHING, null=True)
    job_title = models.CharField(max_length=500)
    degree = models.CharField(max_length=500)
    biography = models.TextField()

class Patient(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    SEX_OPTIONS = [
        (MALE, 'Masculino'),
        (FEMALE, 'Femenino'),
    ]
    
    INCLUSIVE = 'IN'
    SPECUALIZED = 'SP'
    REGULAR = 'RE'
    TYPES_OPTIONS = [
        (INCLUSIVE, 'Inclusiva'),
        (SPECUALIZED, 'Especializada'),
        (REGULAR, 'Regular'),
    ]
    
    URBAN = 'UB'
    RURAL = 'RU'
    PARISH_OPTIONS = [
        (URBAN, 'Urbana'),
        (RURAL, 'Rural'),
    ]

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    identity_card = models.CharField(max_length=10)
    birth = models.DateField()
    sex = models.CharField(max_length=1, choices=SEX_OPTIONS, default=MALE)
    registration_date = models.DateTimeField(auto_now_add=True)
    country_origin = models.CharField(max_length=150)
    province = models.CharField(max_length=100)
    canton = models.CharField(max_length=100)
    educational_institution_type = models.CharField(max_length=2, choices=TYPES_OPTIONS, default=SPECUALIZED)
    educational_institution = models.CharField(max_length=400)
    parish_type = models.CharField(max_length=2, choices=PARISH_OPTIONS, default=URBAN)
    bond_desarrollo_humano = models.BooleanField()
    bond_joaquin_gallegos = models.BooleanField()
    alimony = models.BooleanField()
    jubilee_pension = models.BooleanField()
    montepio = models.BooleanField()
    representatives = models.ManyToManyField(User, through='Relationship')

class Relationship(models.Model):
    representative = models.ForeignKey(User, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    relationship = models.CharField(max_length=100)

class Direction(models.Model):
    main_street = models.CharField(max_length=250)
    secondary_street = models.CharField(max_length=250, null=True)
    house_number = models.CharField(max_length=5, null=True)
    reference = models.TextField()

class Disability_card(models.Model):
    HEARING = 'HE'
    PHYSICAL = 'PH'
    INTELLECTUAL = 'IN'
    LANGUAGE = 'LA'
    PSYCOSOCIAL = 'PS'
    VISUAL = 'VI'
    DISABILITY_OPTIONS = [
        (HEARING, 'Discapacidad Auditiva'),
        (PHYSICAL, 'Discapacidad Física'),
        (INTELLECTUAL, 'Discapacidad Intelectual'),
        (LANGUAGE, 'Discapacidad del Lenguaje'),
        (PSYCOSOCIAL, 'Discapacidad Psicosocial'),
        (VISUAL, 'Discapacidad Visual'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    disability_type = models.CharField(max_length=2, choices=DISABILITY_OPTIONS)
    disability_description = models.TextField()
    disability_percentage = models.PositiveSmallIntegerField()

class Forum_entry(models.Model):
    representative = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    subject = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

class Forum_response(models.Model):
    entry = models.ForeignKey(Forum_entry, on_delete=models.CASCADE, null=True)
    #response = models.ForeignKey(Forum_response, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    response = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    like = models.PositiveIntegerField(default=0)
    dislike = models.IntegerField(default=0)

class Therapy_live(models.Model):
    therapist = models.ForeignKey(Forum_entry, on_delete=models.CASCADE, null=True)
    therapy_date = models.DateField()
    registration_date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=500)
    url = models.CharField(max_length=500)

class Therapy_local(models.Model):
    therapist = models.ForeignKey(Forum_entry, on_delete=models.CASCADE, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    therapy_date = models.DateField()
    registration_date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=500)
    url = models.CharField(max_length=500)

class Tip(models.Model):
    HEARING = 'HE'
    PHYSICAL = 'PH'
    INTELLECTUAL = 'IN'
    LANGUAGE = 'LA'
    PSYCOSOCIAL = 'PS'
    VISUAL = 'VI'
    DISABILITY_OPTIONS = [
        (HEARING, 'Discapacidad Auditiva'),
        (PHYSICAL, 'Discapacidad Física'),
        (INTELLECTUAL, 'Discapacidad Intelectual'),
        (LANGUAGE, 'Discapacidad del Lenguaje'),
        (PSYCOSOCIAL, 'Discapacidad Psicosocial'),
        (VISUAL, 'Discapacidad Visual'),
    ]

    ACTIVITIES = 'AC'
    PERSONAL = 'PC'
    CATEGORY_OPTIONS = [
        (ACTIVITIES, 'Actividades recreativas'),
        (PERSONAL, 'Cuidado personal'),
    ]

    disability = models.CharField(max_length=2, choices=DISABILITY_OPTIONS)
    category = models.CharField(max_length=2, choices=CATEGORY_OPTIONS)
    subject = models.CharField(max_length=200)
    description = models.CharField(max_length=1500)
    url = models.CharField(max_length=500)

class Therapeutic_center(models.Model):
    name = models.CharField(max_length=100)
    direction = models.ForeignKey('Direction', on_delete=models.DO_NOTHING, null=True)
    phone_number_1 = models.PositiveIntegerField()
    phone_number_2 = models.PositiveIntegerField()
    email = models.EmailField(max_length=250)
    bank_name = models.CharField(max_length=100)
    bank_account = models.CharField(max_length=10)
    bank_id_card = models.CharField(max_length=10)

class Directory(models.Model):
    name = models.CharField(max_length=100)
    direction = models.ForeignKey('Direction', on_delete=models.DO_NOTHING, null=True)
    description = models.CharField(max_length=1500)