from django.urls import path, include
from . import views            # . == path of the file in the same file of url
from . import api

app_name = 'job'

urlpatterns = [
    path('', views.job_list, name='job_list'),              # مابضيفش فيها حاجة علشان لما يدخل فى الملف الرئيسي هيلاقي \job بس وهيعتبره مساره(' ')
    path('add', views.add_job, name='add_job'),
    path('<str:slug>', views.job_detail, name='job_detail'),    # ('<id>') بحدد له مسار واعرف في الرئيسي هلشان ميدخلش فى اللى فوق لما اطلبه والمسار بين الاقواس
                                                                # id سابقا  (slug حاليا لعمل فلتر باسم الوظيفة)
    # api
    path('api/jobs', api.job_list_api, name='job_list_api'),
    path('api/jobs/<int:id>', api.job_detail_api, name='job_detail_api'),

    # Generic (class based views)
    path('api/v2/jobs/', api.JobListApi.as_view(), name='JobListApi'),
    path('api/v2/jobs/<int:id>', api.JobDetail.as_view(), name='JobDetail'),

]
