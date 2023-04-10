from django_filters import FilterSet, CharFilter, DateTimeFilter, ModelMultipleChoiceFilter
from django.forms import DateTimeInput
from .models import Category, Author


class PostFilter(FilterSet):
    title = CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Заголовок:',
    )
    added_after = DateTimeFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        label='Дата создания:',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        )
    )
    category = ModelMultipleChoiceFilter(
        field_name='postCategory',
        queryset=Category.objects.all(),
        label='Категория',
        )

    author = ModelMultipleChoiceFilter(
        field_name='author',
        queryset=Author.objects.all(),
        label='Автор:',
    )