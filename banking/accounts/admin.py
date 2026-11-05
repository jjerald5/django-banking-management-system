from django.contrib import admin

# Register your models here.
from .models import BankAccount, Loan, BankCard, HealthInsurance


@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = (
        'account_number',
        'customer',
        'account_type',
        'balance',
        'interest_rate',
        'status'
    )
    list_filter = ('account_type', 'status')
    search_fields = ('account_number', 'customer__username')


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = (
        'customer',
        'loan_type',
        'sanctioned_amount',
        'outstanding_amount',
        'interest_rate',
        'next_due_date',
        'status'
    )
    list_filter = ('loan_type', 'status')


@admin.register(BankCard)
class BankCardAdmin(admin.ModelAdmin):
    list_display = (
        'customer',
        'card_type',
        'card_variant',
        'last_four_digits',
        'status'
    )
    list_filter = ('card_type', 'status')


@admin.register(HealthInsurance)
class HealthInsuranceAdmin(admin.ModelAdmin):
    list_display = (
        'customer',
        'policy_number',
        'policy_type',
        'coverage_amount',
        'renewal_date',
        'status'
    )
    list_filter = ('policy_type', 'status')