from django.urls import path, include
from . import views    # . == path of the file in the same file of url




urlpatterns = [
    path('',views.job_list),   #مابضيفش فيها حاجة علشان لما يدخل فى الملف الرئيسي هيلاقي \job بس وهيعتبره مساره(' ')
    path('<int:id>',views.job_detail),   # ('<id>') بحدد له مسار واعرف في الرئيسي هلشان ميدخلش فى اللى فوق لما اطلبه والمسار بين الاقواس
    ]