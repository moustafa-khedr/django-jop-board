from django.contrib import admin

# Register your models here.

from .models import jop, Category  #(اعمل استدعاء لملف models  فى ال admin)

admin .site.register(jop)    # (لتسجيل الملف فى صفحة الادمن بيظهر على الصفحة)

admin.site.register(Category)