import graphene

from ..models import Category, Movie
from .schema import CategoryType, MovieType


class CategoryQuery(graphene.ObjectType):
    categories_all = graphene.List(CategoryType)
    category_by_name = graphene.Field(
        CategoryType, name=graphene.String(required=True))

    def resolve_categories_all(self, info, **kwargs):
        return Category.objects.all()

    def resolve_category_by_name(self, info, name):
        return Category.objects.filter(name=name).first()


class MovieQuery(graphene.ObjectType):
    movies_all = graphene.List(MovieType)

    def resolve_movies_all(self, info, **kwargs):
        return Movie.objects.select_related("category")
