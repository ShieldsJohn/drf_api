from rest_framework import generics, permissions
from .models import SavedPost
from .serializers import SavedPostSerializer
from drf_api.permissions import IsOwnerOrReadOnly


class SavedPostList(generics.ListCreateAPIView):
    """
    List all saved posts or create a new saved post
    """
    serializer_class = SavedPostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return SavedPost.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SavedPostDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve and/or delete a saved post
    """
    queryset = SavedPost.objects.all()
    serializer_class = SavedPostSerializer
    permission_classes = [IsOwnerOrReadOnly]
