
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('', root, name="root"),
    path('hey/<str:name>', hey_views, name="hey"),
    path('age-in/<int:end>/<int:birth>', age_in_views),
    path('order-total/<int:burgers>/<int:fries>/<int:drinks>', order_views),
    path('admin/', admin.site.urls),
]
