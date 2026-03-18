
from django.contrib import admin
from django.urls import path
from tasks.views import TaskListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TaskListView.as_view()),
]
