from django.contrib import admin

# Register your models here.
from first_app.models import AcessRecord,Topic,Webpage

admin.site.register(AcessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
