from .models import Member
from rest_framework import viewsets
from .serializers import MemberSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


# ViewSet
class MemberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows member to be viewed or edited.
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


# api_view
@api_view(['GET', 'POST'])
def member_api(request):
    """
    API endpoint that allows member to be viewed or edited made by function.
    """
    if request.method == 'GET':
        members = Member.objects.all()
        serializer = MemberSerializer(members, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)