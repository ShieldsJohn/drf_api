from django.db.models import Count, Case, When, IntegerField
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    """
    List posts or create a post if logged in
    The perform_create method associates the post with the logged in user.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        like_count=Count(Case(When(reactions__reaction_type='like', then=1),
        output_field=IntegerField()), distinct=True),
        funny_count=Count(Case(When(reactions__reaction_type='funny', then=1),
        output_field=IntegerField()), distinct=True),
        sad_count=Count(Case(When(reactions__reaction_type='sad', then=1),
        output_field=IntegerField()), distinct=True),
        cute_count=Count(Case(When(reactions__reaction_type='cute', then=1),
        output_field=IntegerField()), distinct=True),
        celebrate_count=Count(Case(When(reactions__reaction_type='celebrate', then=1),
        output_field=IntegerField()), distinct=True),

        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'owner__followed__owner__profile',
        'reactions__owner__profile',
        'owner__profile',
        'reactions__reaction_type',
    ]

    search_fields = [
        'owner__username',
        'title',
    ]

    ordering_fields = [
        'like_count',
        'funny_count',
        'sad_count',
        'cute_count',
        'celebrate_count',
        'comments_count',
        'reactions__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        like_count=Count(Case(When(reactions__reaction_type='like', then=1),
        output_field=IntegerField()), distinct=True),
        funny_count=Count(Case(When(reactions__reaction_type='funny', then=1),
        output_field=IntegerField()), distinct=True),
        sad_count=Count(Case(When(reactions__reaction_type='sad', then=1),
        output_field=IntegerField()), distinct=True),
        cute_count=Count(Case(When(reactions__reaction_type='cute', then=1),
        output_field=IntegerField()), distinct=True),
        celebrate_count=Count(Case(When(reactions__reaction_type='celebrate', then=1),
        output_field=IntegerField()), distinct=True),

        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
