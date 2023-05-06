
"""Perexma models in database"""

from django.db import models
from django.utils import timezone


# region Base and Params models"

class BaseModel(models.Model):
    """Base model for db structure"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        """Setting abstract class to prevent Django to create a table for it."""
        abstract = True

    def delete(self, using=None, keep_parents=False):
        """Soft-delete any record"""
        self.deleted_at = timezone.now()
        self.deleted = True
        self.save()

    def undelete(self):
        """Undo soft-delete operation"""
        self.deleted_at = None
        self.deleted = False
        self.save()


class Category(BaseModel):
    """Category when a transaction fits in"""

    name = models.CharField(max_length=60)


class Currency(BaseModel):
    """Currency for a transaction, such as COP, USD, etc."""

    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)


class Resource(BaseModel):
    """Resources"""

    title = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=10, decimal_places=2)

# endregion


# region Logic models

class User(BaseModel):
    """User that interacts with the app"""

    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    verified = models.BooleanField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    active = models.BooleanField()


class Transaction(BaseModel):
    """Transaction to represent movements for expenses or incomes"""

    is_expense = models.BooleanField()
    is_income = models.BooleanField()
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT
    )
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255, null=True)
    currency = models.ForeignKey(
        Currency,
        on_delete=models.PROTECT
    )
    value = models.DecimalField(max_digits=10, decimal_places=2)
    resource = models.ForeignKey(
        Resource,
        on_delete=models.PROTECT,
        null=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT
    )
    location = models.CharField(max_length=100)


class Savings(BaseModel):
    """Savings that shouldn't be touched... as possible."""

    name = models.CharField(max_length=40)
    description = models.CharField(max_length=255)
    currency = models.ForeignKey(
        Currency,
        on_delete=models.PROTECT
    )
    value = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT
    )


class PendingBills(BaseModel):
    """Pending bills for current cycle"""

    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT
    )
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    link = models.CharField(max_length=255, null=True)
    due_date = models.DateField()
    value = models.DecimalField(max_digits=10, decimal_places=2)


class Settings(BaseModel):
    """Specific setup for current user"""

    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT
    )
    cycle = models.CharField(
        max_length=1,
        choices=[
            ('F', 'Fortnight'),  # period of 2 weeks
            ('W', 'Weekly'),
            ('M', 'Month'),
            ('Y', 'Year'),
        ]
    )

# endregion
