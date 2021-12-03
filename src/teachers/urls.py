"""lms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.urls import include, path


from teachers.views import create_teacher, get_teachers, update_teacher, delete_teacher

urlpatterns = [

    path('', get_teachers, name='list_teacher'),
    path('create', create_teacher, name='create_teacher'),
    path('update/<int:id>', update_teacher, name='update_teacher'),
    path('delete/<int:id>', delete_teacher, name='delete_teacher'),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

