from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserListModel
from .serializer import UserSerializer

# View to render the HTML template
def user_list(request):
    return render (request, 'user_list.html')

# API view to handle list and create operations for users
class UserList(APIView):
    def get(self, request):
        users = UserListModel.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API view to handle retrieve and delete operations for a specific user
# class UserDetail(APIView):
#     def get(self, request, pk):
#         try:
#             user = UserListModel.objects.get(pk=pk)
#         except UserListModel.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#         serializer = UserSerializer(user)
#         return Response(serializer.data)

#     def delete(self, request, pk):
#         try:
#             user = UserListModel.objects.get(pk=pk)
#         except UserListModel.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#         UserListModel.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
