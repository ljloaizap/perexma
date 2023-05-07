"""Perexma admin module"""

from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from django.utils import timezone

from perexmapp.models import Category


class BaseAdmin(admin.ModelAdmin):
    """Base admin class"""

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        """Filter queryset to exclude soft-deleted records
        and order the list by specified fields, if any."""

        queryset = super().get_queryset(request).filter(deleted=False)
        if self.ordering:
            return queryset.order_by(*self.ordering)
        return queryset

    def delete_queryset(self, request: HttpRequest, queryset: QuerySet[Any]) -> None:
        """Overriding deleted action to apply soft-delete instead of hard-delete"""

        queryset.update(deleted=True, deleted_at=timezone.now())


@admin.register(Category)
class CategoryAdmin(BaseAdmin):
    """Admin class for Category parametrization"""

    # list_display = ('name', )
    fields = ('name', )
    ordering = ('name', )
