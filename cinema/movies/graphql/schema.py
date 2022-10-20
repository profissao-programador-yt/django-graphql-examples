from graphene_django import DjangoObjectType

from ..models import Category, Movie


class CategoryType(DjangoObjectType):

    class Meta:
        model = Category
        fields = "__all__"


class MovieType(DjangoObjectType):

    class Meta:
        model = Movie
        fields = "__all__"
