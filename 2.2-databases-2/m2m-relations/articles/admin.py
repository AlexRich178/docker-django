from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Section, SectionArticle


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        true_list = []
        for form in self.forms:
            if 'is_main' in form.cleaned_data:
                true_list.append(form.cleaned_data['is_main'])
        if true_list.count(True) >= 2:
            raise ValidationError('Главный тег может быть только один!')
        return super().clean()  # вызываем базовый код переопределяемого метода


class SectionArticleInline(admin.TabularInline):
    model = SectionArticle
    formset = RelationshipInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [SectionArticleInline]


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    pass
