from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from .serializers import RegisterSerializer
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(
    method = "post" ,
	operation_summary="Login end point", # summarizes the dropdown in GET
	operation_description="""
	**send post request to this end point will**
	- Login to the system using username and password, test by username=***admin*** password=***@2bdelfatta77*** ...""", 
	responses={200:'login successfully and return token and user data (id , username , email)',
	401: 'for unquthorized (invalid token)' ,
    400 : "for wrong username of password"} ,
    
	#request_body={"username" : "admin" , "password" : "@2bdelfatta77"}
	 request_body=AuthTokenSerializer)
@api_view(["POST"]) 
def login_api(request) : 
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data["user"]
    _ , token = AuthToken.objects.create(user) 
    return Response({
        "user_info" : {
            "id" : user.id, 
            "username" : user.username, 
            "email" : user.email 
            } , 
        "token" : token 
    })
    
@swagger_auto_schema(
    method = "get" ,
	operation_summary="get the user data", # summarizes the dropdown in GET
	operation_description="""
	**send get request will get the user data **
	- you must include the Token on the header of the request """, 
	responses={200:'get the user data successfully',
	401: '(invalid token)' ,
    400 : "not authenticated, no token provided"})
@api_view(["GET"]) 
def get_user_data(request) : 
    user = request.user
    if user.is_authenticated :
        return Response({
            "user_info" : {
                "id" : user.id, 
                "username" : user.username, 
                "email" : user.email 
            }
        })
    return Response({"error" :"not aithenticated"  }, status=400)
@swagger_auto_schema(
    method = "post" ,
	operation_summary="Register end point", # summarizes the dropdown in GET
	operation_description="""
	**send post request to this end point will**
	- Resgister as a new user""", 
	responses={200:'register successfully',
    400 : "for wrong data email ot username are already exists"} ,
    
	 request_body=RegisterSerializer)
@api_view(["POST"]) 
def register_api(request) : 
    serializer = RegisterSerializer (data = request.data) 
    serializer.is_valid(raise_exception=True) 
    user = serializer.save() 
    _ , token = AuthToken.objects.create(user) 
    return Response({
        "user_info" : {
                "id" : user.id, 
                "username" : user.username, 
                "email" : user.email 
            } ,
        "token" : token
    })
    
    
    