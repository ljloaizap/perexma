"""Tests for Category model"""

import pytest
from django.db.utils import DataError, IntegrityError

from perexmapp.models import Category

# pylint: disable=no-member


@pytest.mark.django_db
def test_category_success():
    """Test a category is successfully created"""

    category_name = 'Category Lalo'
    category = Category.objects.create(name=category_name)
    assert category.id is not None
    assert category.name == category_name
    assert category.deleted is False
    assert category.deleted_at is None


@pytest.mark.django_db
def test_category_without_name():
    """Tests when category has no name"""

    with pytest.raises(IntegrityError) as excinfo:
        Category.objects.create(name=None)
        assert 'name' in excinfo.value.message_dict


@pytest.mark.django_db
def test_category_name_exceeds_length():
    """Tests when category name exceeds its length"""

    category = Category.objects.create(name="a" * 60)
    assert len(category.name) <= 60

    with pytest.raises(DataError):
        Category.objects.create(name="a" * 61)


def test_category__str__returns_name():
    """Test __str__ method returns the category name"""

    category = Category()
    category.name = 'CategoryTest'
    assert str(category) == category.name


def test_category_verbose_name_plural():
    """Tests if verbose name plural form is 'Categories'"""

    verbose_name_plural = str(Category.objects.model._meta.verbose_name_plural)
    assert verbose_name_plural == 'Categories'
