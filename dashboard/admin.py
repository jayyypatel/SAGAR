from django.contrib import admin
from .models import Join_us, Publication_pdf, Staff

# Register your models here.
admin.site.register(Staff)
admin.site.register(Join_us)
admin.site.register(Publication_pdf)