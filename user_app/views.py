from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.exceptions import TokenError

# Create your views here.
class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        try:
            # Get the original refresh token
            refresh = request.data.get('refresh')
            
            # Verify and refresh the token
            refresh_token = RefreshToken(refresh)
            
            # Generate new access and refresh tokens
            new_access = str(refresh_token.access_token)
            new_refresh = str(refresh_token)
            
            return Response({
                'access': new_access,
                'refresh': new_refresh
            }, status=status.HTTP_200_OK)
        
        except TokenError:
            # If refresh token is invalid or expired
            return Response({
                'error': 'Invalid or expired refresh token'
            }, status=status.HTTP_401_UNAUTHORIZED)
            
class RegisterView(APIView):
    def post(self, request):
        print("register request", request.data)
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("registered", serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        username=request.data.get('username')
        password=request.data.get('password')
        user = User.objects.filter(username=username).first()
        
        if not user:
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)

        if not user.is_active:
            return Response({"error": "Account is inactive. Please contact support."}, status=status.HTTP_400_BAD_REQUEST)
        if user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                'username': user.username,
                'user_id': user.id,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)