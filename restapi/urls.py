from django.urls import path, include
from . import views

urlpatterns = [
    path("expenses/", views.ExpenseListCreate.as_view(), name="expense-list-create")
]
