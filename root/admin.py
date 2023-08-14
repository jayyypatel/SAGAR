
from django.contrib import admin
from root.models import Doante_us, Donate_receipt, Mailbox

# Register your models here.
admin.site.register(Mailbox)
admin.site.register(Doante_us)
admin.site.register(Donate_receipt)