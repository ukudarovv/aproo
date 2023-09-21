from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

User = get_user_model()


class RegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        username = request.data.get('username')

        existing_user = User.objects.filter(username=username).first()

        if existing_user:
            return Response({"message": "Пользователь уже зарегистрирован."}, status=status.HTTP_400_BAD_REQUEST)

        response = super().create(request, *args, **kwargs)
        user = self.serializer_class.Meta.model.objects.get(pk=response.data['id'])

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        return Response({
            'access_token': access_token,
            'refresh_token': refresh_token
        }, status=status.HTTP_201_CREATED)


class AuthorsView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (permissions.IsAuthenticated,)


class BooksView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticated,)


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticated,)


class AddReviewView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        book_id = kwargs.get('book_id')
        try:
            book = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return Response({"message": "Книга не найдена."}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(book=book, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DeleteReviewView(generics.DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def destroy(self, request, *args, **kwargs):
        review_id = kwargs.get('review_id')
        try:
            review = Review.objects.get(pk=review_id)
        except Review.DoesNotExist:
            return Response({"message": "Отзыв не найден."}, status=status.HTTP_404_NOT_FOUND)

        if review.user != request.user:
            return Response({"message": "Вы не можете удалить данный отзыв."}, status=status.HTTP_403_FORBIDDEN)

        review.delete()
        return Response({"message": "Отзыв удален."}, status=status.HTTP_204_NO_CONTENT)


class CustomTokenObtainPairView(TokenObtainPairView):
    pass

class CustomTokenRefreshView(TokenRefreshView):
    pass
