import graphene

from ..models import Category, Movie
from .schema import CategoryType, MovieType


class CategoryCreate(graphene.Mutation):
    category = graphene.Field(CategoryType)
    error = graphene.Field(graphene.String)

    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String()

    def mutate(self, info, name, **kwargs):
        if len(name) < 5:
            return CategoryCreate(error="Nome muito curto.")

        category_instance = Category.objects.create(name=name, **kwargs)

        return CategoryCreate(category=category_instance)


class CategoryUpdate(graphene.Mutation):
    category = graphene.Field(CategoryType)
    error = graphene.Field(graphene.String)

    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        description = graphene.String()

    def mutate(self, info, id, name, **kwargs):
        category_instance = Category.objects.filter(id=id).first()
        if not category_instance:
            return CategoryUpdate(error="Categoria não encontrada")

        if name and len(name) < 5:
            return CategoryUpdate(error="Nome muito curto.")

        description = kwargs.get("description", None)

        category_instance.name = name if name is not None else category_instance.name
        category_instance.description = description if description is not None else category_instance.description
        category_instance.save()

        return CategoryUpdate(category=category_instance)


class CategoryDelete(graphene.Mutation):
    success = graphene.Field(graphene.String)
    error = graphene.Field(graphene.String)

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, info, id, **kwargs):
        category_instance = Category.objects.filter(id=id).first()
        if not category_instance:
            return CategoryDelete(error="Categoria não encontrada")

        category_instance.delete()
        return CategoryDelete(success="Categoria removida.")


class CategoryMutation(graphene.ObjectType):
    category_create = CategoryCreate.Field()
    category_update = CategoryUpdate.Field()
    category_delete = CategoryDelete.Field()


class MovieCreate(graphene.Mutation):
    movie = graphene.Field(MovieType)
    error = graphene.Field(graphene.String)

    class Arguments:
        category_id = graphene.ID(required=True)
        name = graphene.String(required=True)
        description = graphene.String()

    def mutate(self, info, category_id, name, **kwargs):
        category_instance = Category.objects.filter(id=category_id).first()
        if not category_instance:
            return MovieCreate(error="Categoria não encontrada.")

        movie_instance = Movie.objects.create(
            category=category_instance,
            name=name,
            **kwargs
        )

        return MovieCreate(movie=movie_instance)


class MovieMutation(graphene.ObjectType):
    movie_create = MovieCreate.Field()
