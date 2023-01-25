from django.contrib import admin

# Register your models here.

from .models import Job, Category, Apply  #(اعمل استدعاء لملف models  فى ال admin)

admin.site.register(Job)    # (لتسجيل الملف فى صفحة الادمن بيظهر على الصفحة)

admin.site.register(Category)

admin.site.register(Apply)