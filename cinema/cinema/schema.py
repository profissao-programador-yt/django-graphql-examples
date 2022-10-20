import graphene

from movies.graphql import queries
from movies.graphql import mutations


class Query(queries.CategoryQuery, queries.MovieQuery):
    pass


class Mutation(mutations.CategoryMutation, mutations.MovieMutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
