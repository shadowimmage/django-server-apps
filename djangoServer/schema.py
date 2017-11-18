# Root-level Schema
import graphene

import rttApp.schema

class Query(rttApp.schema.Query, graphene.ObjectType):
    pass

class Mutation(rttApp.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)