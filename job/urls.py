from django.urls import path
from .views import JobCreateView, JobListView, JobUpdateDestoryView, JobApplyView

urlpatterns = [
    path("list/", JobListView.as_view()),
    path("create/", JobCreateView.as_view()),
    path("<int:pk>/", JobUpdateDestoryView.as_view()),
    path("jobs/<int:pk>/apply/", JobApplyView.as_view()),
]
