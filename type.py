from graphene import ObjectType,Int,BigInt,String

class UserObject(ObjectType):
    id =Int()
    name=String()
    contact_email=String()
    mobile=BigInt()