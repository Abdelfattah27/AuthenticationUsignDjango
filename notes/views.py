from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework.authtoken.serializers import AuthTokenSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins , generics
from rest_framework.views import APIView
from .serializers import NoteSerializer
from .models import Note
from rest_framework.permissions import IsAuthenticated 
from rest_framework.decorators import permission_classes
from rest_framework import status

# Create your views here.
# @swagger_auto_schema(
#     method = "get" ,
# 	operation_summary="get the user notes", # summarizes the dropdown in GET
# 	operation_description="""
# 	**send get request will get the user notes **
# 	- you must include the Token on the header of the request """, 
# 	responses={200:'get the user notes successfully',
# 	401: '(invalid token)' ,
#     400 : "not authenticated, no token provided"})
# @api_view(["GET"]) 
# def get_user_notes(request) : 
#     user = request.user
#     if user.is_authenticated :
#         user_notes = user.notes.values()
#         return Response({
#           "notes" : list(user_notes)
#         })
#     return Response({"error" :"not authenticated"  }, status=400)
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
@api_view(["GET" , "POST"])
@permission_classes([IsAuthenticated]) 
def get_create_notes(request) : 
    if request.method == "GET" : 
        try : 
            user  = request.user
            serializer = NoteSerializer(user.notes , many = True) 
            return Response(serializer.data)
        except Exception as ex : 
            return Response({"details" : str(ex)} , status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "POST" : 
        try : 
            user =request.user 
            data = request.data
            data["user"] = user.id
            serializer = NoteSerializer(data = data)
            if serializer.is_valid() : 
                serializer.save()
                return Response(serializer.data)
        except Exception as ex : 
            return Response({"details" : str(ex)} , status=status.HTTP_400_BAD_REQUEST)
        
@api_view(["PUT" , "DELETE" , "GET"])
@permission_classes([IsAuthenticated]) 
def single_note(request , pk) : 
    if request.method == "GET" : 
        try : 
            user = request.user 
            note = Note.objects.get(id = pk) 
            if note.user == user : 
                serializer = NoteSerializer(note)
                return Response(serializer.data)
            else : 
                return Response({"details" : "Not Authorized"} , status=status.HTTP_400_BAD_REQUEST)
        except Note.DoesNotExist : 
            return Response({"details" : 'Not exists'} , status=status.HTTP_404_NOT_FOUND)
        except Exception as ex  : 
            return Response({"details" : str(ex)} , status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == "PUT" : 
        try : 
            user = request.user 
            note = Note.objects.get(id = pk) 
            data = request.data
            data["user"] = user.id
            if note.user == user : 
                serializer = NoteSerializer(instance=note , data = data) 
                if serializer.is_valid() : 
                    serializer.save() 
                    return Response(serializer.data , status=status.HTTP_200_OK)
                else : 
                    return Response({"details" : str(serializer.errors)} , status=status.HTTP_400_BAD_REQUEST)
            else : 
                return Response({"details" : "Not Authorized"} , status=status.HTTP_400_BAD_REQUEST)

        except Note.DoesNotExist : 
            return Response({"details" : 'Not exists'} , status=status.HTTP_404_NOT_FOUND)
        except Exception as ex  : 
            return Response({"details" : str(ex)} , status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == "DELETE" : 
        try : 
            user = request.user 
            note = Note.objects.get(id = pk) 
            if note.user == user : 
                note.delete() 
                return Response({"details" : "deleted successfully" } , status=status.HTTP_204_NO_CONTENT)
            else : 
                return Response({"details" : "Not Authorized"} , status=status.HTTP_400_BAD_REQUEST)
        except Note.DoesNotExist : 
            return Response({"details" : 'Not exists'} , status=status.HTTP_404_NOT_FOUND)
        except Exception as ex  : 
            return Response({"details" : str(ex)} , status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def uploadImage(request , pk) : 
    try:
        user = request.user
        note = Note.objects.get(id = pk)
        if note.user == user : 
            image  = request.FILES.get("image")
            note.image.save(image.name, image)
            note.save()
            serializer = NoteSerializer(note) 
            return Response(serializer.data)
        else : 
            return Response({"details" : "Not Authorized"} , status=status.HTTP_400_BAD_REQUEST)      
    except Exception as ex:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
                


