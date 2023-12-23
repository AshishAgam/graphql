from graphene import Schema
from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp,make_playground_handler
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from database import prepare_database
from queries import Query
from mutations import Mutation
schema=Schema(query=Query, mutation=Mutation)

app=FastAPI()

@app.on_event("startup")
def startup_event():
    prepare_database()

app.mount("/gql", GraphQLApp(
    schema=schema,
    on_get=make_playground_handler()
))
