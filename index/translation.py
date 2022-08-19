from modeltranslation.translator import TranslationOptions, register

from index.models import Category, RoomsModel, Model, Responsible, Product


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(RoomsModel)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('rooms', 'floor')


@register(Model)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Responsible)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('fullname', 'description')


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('description', 'status', 'responsible_person')
