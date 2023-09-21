from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegistrationView.as_view()),
    path('login/', CustomTokenObtainPairView.as_view()),
    path('token/refresh/', CustomTokenRefreshView.as_view()),
    path('books/', BooksView.as_view()),
    path('books/<int:pk>/', BookDetailView.as_view()),
    path('authors/', AuthorsView.as_view()),
    path('books/<int:book_id>/review/', AddReviewView.as_view()),
    path('books/review/<int:review_id>/', DeleteReviewView.as_view()),
]
