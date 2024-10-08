from django.urls import path

from .views import (
    PatientListView,
    PatientCreateView,
    PatientView,
    PatientUpdateView,
    PatientDeleteView
)

urlpatterns = [
    path('', PatientListView.as_view(), name='patient_list'),
    path('patient/new/', PatientCreateView.as_view(), name='patient_create'),
    path('patient/<int:pk>/', PatientView.as_view(), name='patient_detail'),
    path('patient/<int:pk>/edit/', PatientUpdateView.as_view(), name='patient_edit'),
    path('patient/<int:pk>/delete/',
         PatientDeleteView.as_view(),
         name='patient_delete',
         ),
]
