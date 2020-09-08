from django.contrib import admin
from .models import User, Patient, Relationship, Direction, Disability_card, Disability, Forum_entry, Forum_response, Therapy_live, Therapy_local, Tip, Therapeutic_center, Directory

admin.site.register(User)
admin.site.register(Patient)
admin.site.register(Relationship)
admin.site.register(Direction)
admin.site.register(Disability)
admin.site.register(Disability_card)
admin.site.register(Forum_entry)
admin.site.register(Forum_response)
admin.site.register(Therapy_live)
admin.site.register(Therapy_local)
admin.site.register(Tip)
admin.site.register(Therapeutic_center)
admin.site.register(Directory)