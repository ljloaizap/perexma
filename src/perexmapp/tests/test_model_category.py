"""Tests for Category model"""

import pytest
from django.db.utils import DataError, IntegrityError

from perexmapp.models import Category, BaseModel

# pylint: disable=no-member


@pytest.fixture
def category():
    """Fixture for category creation"""

    obj_category = Category.objects.create(name='Test Category')
    yield obj_category
    obj_category.delete()


@pytest.mark.django_db
def test_category_success(category):
    """Test a category is successfully created"""

    assert category.id is not None
    assert 0 < len(category.name) < 61
    assert category.deleted is False
    assert category.deleted_at is None


@pytest.mark.django_db
def test_category_without_name():
    """Tests when category has no name"""

    with pytest.raises(IntegrityError):
        Category.objects.create(name=None)


@pytest.mark.django_db
def test_category_name_exceeds_length():
    """Tests when category name exceeds its length"""

    with pytest.raises(DataError):
        Category.objects.create(name="a" * 61)


@pytest.mark.django_db
def test_category_soft_delete(category):
    """Test soft-delete is performed when delete action is called"""

    category.delete()
    assert category.deleted is True
    assert category.deleted_at is not None


@pytest.mark.django_db
def test_category_undo_soft_delete(category):
    """Undoing soft-deletion of category entity"""

    category.undelete()
    assert category.deleted is False
    assert category.deleted_at is None


def test_category__str__returns_name():
    """Test __str__ method returns the category name."""

    obj_category = Category()
    obj_category.name = 'CategoryTest'
    assert str(obj_category) == obj_category.name


def test_category_verbose_name_plural():
    """Tests if verbose name plural form is 'Categories'."""

    verbose_name_plural = str(Category.objects.model._meta.verbose_name_plural)
    assert verbose_name_plural == 'Categories'


def test_category_inherits_base_model():
    """Checking that Category model inherits from BaseModel"""
    assert issubclass(Category, BaseModel)
