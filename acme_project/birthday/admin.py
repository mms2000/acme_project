from django.contrib import admin

from .models import Birthday


admin.site.empty_value_display = 'Не задано'


class BirthdayAdmin(admin.ModelAdmin):
    pass


admin.site.register(Birthday, BirthdayAdmin)
