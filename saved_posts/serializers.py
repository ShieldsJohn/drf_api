from rest_framework import serializers
from .models import SavedPost


class SavedPostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    post_title = serializers.ReadOnlyField(source='post.title')

    class Meta:
        model = SavedPost
        fields = ['id', 'user', 'post_title', 'post', 'saved_at']
