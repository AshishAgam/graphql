from graphene import Mutation,Field,ObjectType,BigInt,String,Int,Boolean
from database import Session
from models import User
from type import UserObject


class AddUser(Mutation):
    class Arguments:
        name=String(required=True)
        contact_email=String(required=True)
        mobile=BigInt(required=True)
        
    user=Field(lambda:UserObject) 
    
    @staticmethod
    def mutate(root, info, name, contact_email,mobile):
        user =User(name=name,contact_email=contact_email,mobile=mobile)
        session= Session()
        session.add(user)
        session.commit()
        session.refresh(user)
        return AddUser(user=user)
    
class DeleteUser(Mutation):
    class Arguments:
        id=Int(required=True)
        
    success=Boolean()
    
    @staticmethod
    def mutate(root,info,id):
        session=Session()
        user=session.query(User).filter(User.id==id).first()
        
        if not user:
            raise Exception("user not found")
        
        session.delete(user)
        session.commit()
        session.close()
        return DeleteUser(success=True)
    
    
class Mutation(ObjectType):
    add_user=AddUser.Field()
    delete_user=DeleteUser.Field()
    
    
