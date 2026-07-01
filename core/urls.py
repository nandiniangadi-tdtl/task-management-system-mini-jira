from django.urls import path
from .views import *

urlpatterns = [
    path('create-project/', CreateProject.as_view()),
    path('create-task/', CreateTask.as_view()),
    path('update-status/<int:pk>/', UpdateStatus.as_view()),
    path('add-comment/', AddComment.as_view()),
    path('upload/', UploadAttachment.as_view()),
    path('task-history/', TaskHistoryList.as_view()),
]