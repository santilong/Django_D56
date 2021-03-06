"""Django_D56 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01.views import students,fenye
from app02 import views as v2
from app03 import views as v3

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^students.html$', students.students),
    url(r'^addstudent.html$', students.addstudent),
    url(r'^delstudent.html$', students.delstudent),
    url(r'^editstuinfo.html$', students.editstuinfo),
    url(r'^fenye1.html$', fenye.fenye1),
    url(r'^fenye2.html$', fenye.fenye2),
    url(r'^fenye3.html$', fenye.fenye3),
    url(r'^f1.html$', v2.f1),
    url(r'^users.html$', v3.users),
    url(r'^addusers.html$', v3.addusers),
    url(r'^edituser-(\d+)', v3.edituser),

]
