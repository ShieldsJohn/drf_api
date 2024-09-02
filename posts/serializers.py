from rest_framework import serializers
from posts.models import Post
from reactions.models import Reaction
from reactions.constants import LIKE_REACTION_TYPE


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    reaction_id = serializers.SerializerMethodField()
    like_id = serializers.SerializerMethodField()
    like_count = serializers.ReadOnlyField()
    funny_count = serializers.ReadOnlyField()
    sad_count = serializers.ReadOnlyField()
    cute_count = serializers.ReadOnlyField()
    celebrate_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size larger than 2MB!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_reaction_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            reaction = Reaction.objects.filter(
                owner=user, post=obj
            ).first()
            return reaction.id if reaction else None
        return None

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Reaction.objects.filter(
                owner=user, post=obj, reaction_type=LIKE_REACTION_TYPE
            ).first()
            return like.id if like else None
        return None

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'caption', 'image', 'image_filter',
            'reaction_id', 'like_id', 'like_count', 'funny_count',
            'sad_count', 'cute_count', 'celebrate_count',
            'comments_count',
        ]
