import patterns as patterns
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path
from .  import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name = 'home'),
    path('addnews', views.addnews, name='addnews'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('shownews/<int:id>', views.shownews, name='shownews'),
    path('allnews',views.allnews, name = 'allnews'),\
    path('adbout-us',views.about, name = 'adbout-us'),
    path('backsaid',views.backsaid, name = 'backsaid'),
]
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
media_root = getattr(settings, 'MEDIA_ROOT', '/media')
