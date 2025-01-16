# import graphene
# from graphene_django import DjangoObjectType
#
# from apps.models import Product
#
# class CategoryType(DjangoObjectType):
#     class Meta:
#         model = Product
#         fields = ("id", "name", "price")
#
# class Query(graphene.ObjectType):
#     category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))
#     def resolve_category_by_name(root, info, name):
#         try:
#             return Product.objects.get(name=name)
#         except Product.DoesNotExist:
#             return None
#
# schema = graphene.Schema(query=Query)
from django.forms.models import ModelForm
# -------------------------------------

# cookbook/ingredients/schema.py
from graphene import relay, ObjectType, Schema
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
import graphene
from graphene_django import DjangoObjectType

from apps.models import Category, Ingredient , Question


# Graphene will automatically map the Category model's fields onto the CategoryNode.
# This is configured in the CategoryNode's Meta class (as you can see below)
class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['name', 'ingredients']
        interfaces = (relay.Node, )


class IngredientNode(DjangoObjectType):
    class Meta:
        model = Ingredient
        # Allow for some more advanced filtering here
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'notes': ['exact', 'icontains'],
            'category': ['exact'],
            'category__name': ['exact'],
        }
        interfaces = (relay.Node, )


# class Query(ObjectType):
#     category = relay.Node.Field(CategoryNode)
#     all_categories = DjangoFilterConnectionField(CategoryNode)
#
#     ingredient = relay.Node.Field(IngredientNode)
#     all_ingredients = DjangoFilterConnectionField(IngredientNode)


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("id", "question")

class Query(graphene.ObjectType):
    questions = graphene.List(QuestionType)
    question_by_id = graphene.Field(QuestionType, id=graphene.String())

    def resolve_questions(root, info, **kwargs):
        return Question.objects.all()

    def resolve_question_by_id(root, info, id):
        return Question.objects.get(pk=id)

schema = Schema(query=Query)