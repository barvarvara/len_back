# from rest_framework import permissions
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework_simplejwt.authentication import JWTAuthentication
#
#
# class RegisterUserView(APIView):
#     def post(self, request):
#         data = request.data
#         return
#
#
# class RetrieveUserView(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#     authentication_classes = [JWTAuthentication]
#
#     def get(self, request, format=None):
#         content = {
#             'user': str(request.user),
#             'auth': str(request.auth),
#         }
#
#         return Response(content)
