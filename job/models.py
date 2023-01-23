from django.db import models

# Create your models here.
'''
django model field :
    - html widget   (  علشان يعرض حاجة تاخذ حروف html افضل شكل فى )
    - validation   (الحدود بتاعته 100 حرف)
    - D_B size   (انسب حجم داخل دانا بيز)


'''
JOP_TYPE =(
     ("Full-Time","Full-Time"),
     ("Part-Time","Part-Time",),
     )


class jop(models.Model):  # is a table in DB(يكافئ جدول)
     title = models.CharField(max_length=100)  # column in DB(يكافئ عمود )  max-length = max char in field
     #location
     jop_type = models.CharField(max_length=15, choices=JOP_TYPE)
     description = models.TextField(max_length= 1000)
     Published_on = models.DateTimeField(auto_now=True)
     Vacancy = models.IntegerField(default=1)
     salary = models.IntegerField(default=0)
     experience = models.IntegerField(default=1)


     def __str__(self):
          return self.title
