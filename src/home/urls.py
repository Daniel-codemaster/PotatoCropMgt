from django.urls import path

from . import views

urlpatterns = [
    path("", views.index_view, name="index"),
    path("fertiliser", views.fertilizer_pred_view),
    path("irrigation", views.irrigation_shedule_pred_view),
]