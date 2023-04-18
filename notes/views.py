from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework.authtoken.serializers import AuthTokenSerializer
from drf_yasg.utils import swagger_auto_schema

# Create your views here.
@swagger_auto_schema(
    method = "get" ,
	operation_summary="get the user notes", # summarizes the dropdown in GET
	operation_description="""
	**send get request will get the user notes **
	- you must include the Token on the header of the request """, 
	responses={200:'get the user notes successfully',
	401: '(invalid token)' ,
    400 : "not authenticated, no token provided"})
@api_view(["GET"]) 
def get_user_notes(request) : 
    user = request.user
    if user.is_authenticated :
        user_notes = user.notes.values()
        return Response({
          "notes" : list(user_notes)
        })
    return Response({"error" :"not authenticated"  }, status=400)
# @swagger_auto_schema(
#     method = "post" ,
# 	operation_summary="synchronize notes", # summarizes the dropdown in GET
# 	operation_description="""
# 	**send post request with the notes updated **
# 	- you must include the Token on the header of the request """, 
# 	responses={200:'get the user notes successfully',
# 	401: '(invalid token)' ,
#     400 : "not authenticated, no token provided"})
# # @api_view(["POST"])
# # def synchronize_notes(request) : 
# #     # TODO Update note by id 
# #     # TODO create new note
# #     # TODO delete note by id