from django.contrib import admin
from .models import NewsList, comment, backsaids


admin.site.register(NewsList)
admin.site.register(comment)
admin.site.register(backsaids)
# Register your models here.
