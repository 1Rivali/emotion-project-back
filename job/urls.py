from django.urls import path
from .views import JobCreateView, JobListView, JobUpdateDestoryView

urlpatterns = [
    path('list/', JobListView.as_view()),
    path('create/', JobCreateView.as_view()),
    path('<int:pk>/', JobUpdateDestoryView.as_view()),
]
