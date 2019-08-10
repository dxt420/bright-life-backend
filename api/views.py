from bl.models import *
from api.serializers import *
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
# class ApplicantListView(generics.ListAPIView):
#     """
#             get:
#                 Search or get applicants
#     """
#     queryset = Applicant.objects.all()
#     serializer_class = ApplicantSerializer


class ApplicantListCreateView(generics.ListCreateAPIView):
    """
            create:
                new applicants
            get:
                Search or get applicants
                You can search using:
                    :param email
                    :param username
    """
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer
    # filter_backends = (DjangoFilterBackend,)
    # filterset_fields = ('full_name', 'phone')


class ApplicantDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
            get:
                get a specific user
            delete:
                Remove an existing user.
            patch:
                Update one or more fields on an existing user.
            put:
                Update a user.
    """
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer


class IDCreateView(generics.ListCreateAPIView):
   
    queryset = Identity.objects.all()
    serializer_class = IdentitySerializer

class IDDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Identity.objects.all()
    serializer_class = IdentitySerializer


  