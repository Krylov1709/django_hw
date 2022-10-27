from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        tag_amount = 0
        for form in self.forms:
            if form.cleaned_data['is_main']:
                tag_amount += 1
        if tag_amount == 0:
            raise ValidationError('Укажите какой раздел основной')
        elif tag_amount > 1:
            raise ValidationError('Основным может быть только один раздел')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 0
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass
