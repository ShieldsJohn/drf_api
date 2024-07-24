from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'subject', 'message', 'created_at']

    def user_authentication(self, instance):
        """
        Return an error message if user not authenticated
        """
        request = self.context.get('request')
        if not request.user.is_authenticated:
            return {"detail": "Please sign in to contact us."}
        else:
            return super().user_authentication(instance)
            