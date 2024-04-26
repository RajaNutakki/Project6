from . import views
from django.urls import path
app_name = 'Mimeapp'
urlpatterns = [
    path('html',views.htmlview.as_view(),name='htmlview'),
    path('excel',views.excelview.as_view(),name='excel.view'),
    path('xml',views.xmlview.as_view(),name='xmlview'),
]