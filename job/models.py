from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
'''
django model field :
    - html widget   (  علشان يعرض حاجة تاخذ حروف html افضل شكل فى )
    - validation   (الحدود بتاعته 100 حرف)
    - D_B size   (انسب حجم داخل دانا بيز)
'''

JOP_TYPE = (
    ("Full-Time", "Full-Time"),
    ("Part-Time", "Part-Time",),
)


def image_upload(instance, filename):  # (costmize the image to save and upload)
    imagename, extension = filename.split(".")
    return "jobs/%s.%s" % (instance.id, extension)  # (ممكن احط . اى حاجة من الموديل غير id)


class Job(models.Model):  # is a table in DB(يكافئ جدول)
    owner = models.ForeignKey(User, related_name='job_owner',on_delete=models.CASCADE)
    title = models.CharField(max_length=100)  # column in DB(يكافئ عمود )  max-length = max char in field
    # location
    job_type = models.CharField(max_length=15, choices=JOP_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)

    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)   ## logic
        super(Job, self).save(*args, **kwargs)    #to inharite

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Apply(models.Model):
    job = models.ForeignKey(Job , related_name='apply_job', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
