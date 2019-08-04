from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
from api.views import *
urlpatterns = [
    path('applicants/', ApplicantListCreateView.as_view(), name='applicants'),
    path('applicant/<uuid:pk>/',  ApplicantDetailView.as_view(), name='applicant_detail'),
    path('', include(router.urls))
]