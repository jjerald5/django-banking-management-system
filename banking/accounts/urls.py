from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('account/<int:account_id>/',views.account_details,name='account_details'),
    path('loan/<int:loan_id>/',views.loan_details,name='loan_details'),
    path('card/<int:card_id>/',views.card_details,name='card_details'),
    path('insurance/<int:insurance_id>/',views.insurance_details,name='insurance_details'),
]