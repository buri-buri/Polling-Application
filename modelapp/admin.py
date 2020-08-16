from django.contrib import admin
from modelapp import models
# Register your models here.
admin.site.register([
    models.Question,
    models.Choice,
])