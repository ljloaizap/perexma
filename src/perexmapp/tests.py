import pytest
from django.db.utils import DataError

from perexmapp.models import Category

# pylint: disable=no-member


@pytest.mark.django_db
def test_category_name_exceeds_length():
    """Tests when category name exceeds its length"""

    category = Category.objects.create(name="a" * 60)
    assert len(category.name) <= 60

    with pytest.raises(DataError):
        Category.objects.create(name="a" * 61)
