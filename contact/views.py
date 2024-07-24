from rest_framework import generics, permissions
from .models import Contact
from .serializers import ContactSerializer


class ContactList(generics.ListCreateAPIView):
    """
    View to create and list contacts
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]


class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete a contact by id
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]
