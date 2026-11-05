from django.db import models
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator

# Create your models here.
# 1. Bank Account Model
class BankAccount(models.Model):

    ACCOUNT_TYPES = [
        ('savings', 'Savings Account'),
        ('current', 'Current Account'),
    ]

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('closed', 'Closed'),
    ]

    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='bank_accounts'
    )

    account_number = models.CharField(max_length=20, unique=True)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPES)
    balance = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0)]
    )
    interest_rate = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0)]
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active'
    )

    def __str__(self):
        return f"{self.account_type} - {self.account_number}"


# 2. Loan Model
class Loan(models.Model):

    LOAN_TYPES = [
        ('personal', 'Personal Loan'),
        ('home', 'Home Loan'),
        ('vehicle', 'Vehicle Loan'),
        ('education', 'Education Loan'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('active', 'Active'),
        ('closed', 'Closed'),
        ('rejected', 'Rejected'),
    ]

    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='loans'
    )

    loan_type = models.CharField(max_length=20, choices=LOAN_TYPES)
    sanctioned_amount = models.DecimalField(max_digits=15, decimal_places=2)
    outstanding_amount = models.DecimalField(max_digits=15, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    next_due_date = models.DateField(null=True, blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    def __str__(self):
        return f"{self.loan_type} Loan - {self.customer}"


# 3. Bank Card Model
class BankCard(models.Model):

    CARD_TYPES = [
        ('credit', 'Credit Card'),
        ('debit', 'Debit Card'),
    ]

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('blocked', 'Blocked'),
        ('expired', 'Expired'),
    ]

    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='bank_cards'
    )

    card_type = models.CharField(max_length=10, choices=CARD_TYPES)
    card_variant = models.CharField(max_length=50)
    last_four_digits = models.CharField(max_length=4)

    credit_limit = models.DecimalField(
        max_digits=15, decimal_places=2, default=0
    )
    used_credit = models.DecimalField(
        max_digits=15, decimal_places=2, default=0
    )

    daily_limit = models.DecimalField(
        max_digits=15, decimal_places=2, default=0
    )
    used_today = models.DecimalField(
        max_digits=15, decimal_places=2, default=0
    )

    payment_due_date = models.DateField(null=True, blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active'
    )

    @property
    def available_credit(self):
        return max(self.credit_limit - self.used_credit, 0)

    @property
    def available_today(self):
        return max(self.daily_limit - self.used_today, 0)

    def __str__(self):
        return f"{self.get_card_type_display()} - {self.last_four_digits}"


# 4. Health Insurance Model
class HealthInsurance(models.Model):

    POLICY_TYPES = [
        ('individual', 'Individual'),
        ('family', 'Family Floater'),
        ('senior', 'Senior Citizen'),
    ]

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('cancelled', 'Cancelled'),
    ]

    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='health_insurances'
    )

    policy_number = models.CharField(max_length=30, unique=True)
    policy_type = models.CharField(max_length=20, choices=POLICY_TYPES)
    coverage_amount = models.DecimalField(max_digits=15, decimal_places=2)
    renewal_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active'
    )

    def __str__(self):
        return f"{self.policy_number} - {self.customer}"