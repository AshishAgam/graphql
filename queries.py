from graphene import ObjectType,List,Field,Int,Boolean
from type import UserObject
from models import User
from database import Session
from graphql import GraphQLError
class Query(ObjectType):
    users=List(UserObject)
    user=Field(UserObject,id=Int(required=True))
    
    get_status=Field(UserObject,id=Int(required=True))
    
    
    @staticmethod
    def resolve_get_status(root,info,id):
        check_user= Session().query(User).filter(User.id==id).first()
        if not check_user:
            raise GraphQLError ("not found")
        else:
            return True
    

    
    
    @staticmethod
    def resolve_user(root,info,id):
        return Session().query(User).filter(User.id==id).first()
    
    @staticmethod
    def resolve_users(root,info):
        return  Session().query(User).all()
    
