import pytest

from django.db.utils import IntegrityError, DataError
from perexmapp.models import Currency, BaseModel

# pylint: disable=no-member


@pytest.fixture
def currency():
    """PH"""

    obj_currency = Currency.objects.create(code="ABC", name="CurrencyABC")
    yield obj_currency
    obj_currency.delete()


@pytest.mark.django_db
def test_currency_success(currency):
    """PH"""

    assert currency.id is not None
    assert 0 < len(currency.code) < 11
    assert 0 < len(currency.name) < 51
    assert currency.deleted is False
    assert currency.deleted_at is None


@pytest.mark.django_db
def test_currency_without_code_or_name():
    """PH"""

    with pytest.raises(IntegrityError):
        Currency.objects.create(code=None, name=None)


@pytest.mark.django_db
def test_currency_name_or_code_exceed_length():
    """PH"""

    with pytest.raises(DataError):
        Currency.objects.create(
            code='*' * 11,
            name='*' * 51
        )


@pytest.mark.django_db
def test_currency_soft_delete(currency):
    """PH"""

    currency.delete()
    assert currency.deleted is True
    assert currency.deleted_at is not None


@pytest.mark.django_db
def test_currency_undo_soft_delete(currency):
    """PH"""

    currency.undelete()
    assert currency.deleted is False
    assert currency.deleted_at is None


def test_currency__str__returns_code():
    """Test __str__ method returns the currency code."""
    obj_currency = Currency(code="XYZ")
    assert str(obj_currency) == obj_currency.code


def test_currency_verbose_name_plural():
    """PH"""
    assert 'Currencies' == Currency()._meta.verbose_name_plural


def test_currency_inherits_base_model():
    """PH"""
    assert issubclass(Currency, BaseModel)
