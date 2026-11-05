from django.shortcuts import render, get_object_or_404
#from django.contrib.auth.decorators import login_required

from .models import BankAccount, Loan, BankCard, HealthInsurance

# Create your views here.
def dashboard(request):
    if request.user.is_staff:
        accounts = BankAccount.objects.all()
        loans = Loan.objects.all()
        cards = BankCard.objects.all()
        insurances = HealthInsurance.objects.all()

    else:
        accounts = BankAccount.objects.filter(customer=request.user)
        loans = Loan.objects.filter(customer=request.user)
        cards = BankCard.objects.filter(customer=request.user)
        insurances = HealthInsurance.objects.filter(customer=request.user)

    context = {
        'savings_accounts': accounts.filter(account_type='savings'),
        'current_accounts': accounts.filter(account_type='current'),

        'loans': loans,

        'credit_cards': cards.filter(card_type='credit'),
        'debit_cards': cards.filter(card_type='debit'),

        'insurances': insurances,
    }

    return render(request, 'dashboard.html', context)

def account_details(request, account_id):

    if request.user.is_staff:
        account = get_object_or_404(
            BankAccount,
            id=account_id
        )
    else:
        account = get_object_or_404(
            BankAccount,
            id=account_id,
            customer=request.user
        )

    return render(request,
        'account_details.html',
        {'account': account}
    )

# Loan Details

def loan_details(request, loan_id):

    if request.user.is_staff:
        loan = get_object_or_404(Loan, id=loan_id)
    else:
        loan = get_object_or_404(
            Loan,
            id=loan_id,
            customer=request.user
        )

    return render(
        request,
        'loan_details.html',
        {'loan': loan}
    )


# Credit Card and Debit Card Details

def card_details(request, card_id):

    if request.user.is_staff:
        card = get_object_or_404(BankCard, id=card_id)
    else:
        card = get_object_or_404(
            BankCard,
            id=card_id,
            customer=request.user
        )

    return render(
        request,
        'card_details.html',
        {'card': card}
    )


# Health Insurance Details

def insurance_details(request, insurance_id):

    if request.user.is_staff:
        policy = get_object_or_404(
            HealthInsurance,
            id=insurance_id
        )
    else:
        policy = get_object_or_404(
            HealthInsurance,
            id=insurance_id,
            customer=request.user
        )

    return render(
        request,
        'insurance_details.html',
        {'policy': policy}
    )