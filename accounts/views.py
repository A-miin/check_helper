from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView

from accounts.serializers import UserSerializer, AddDeleteDiseaseUserSerializer
from rest_framework import status
from rest_framework.response import Response


class ListCreateUsersAPIView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()

    def get(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response({'detail': _('You do not have permission to perform this action.')},
                            status=status.HTTP_403_FORBIDDEN)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RetrieveUpdateDestroyUsersAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()

    def get_object(self):
        user = super(RetrieveUpdateDestroyUsersAPIView, self).get_object()
        if self.request.user.is_staff:
            return user
        else:
            return self.request.user


class AddDeleteDiseaseAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AddDeleteDiseaseUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        user.diseases.add(*serializer.validated_data['ids'])
        return Response({'message': _('Болезни добавлены')}, status=200)

    def delete(self, request, *args, **kwargs):
        serializer = AddDeleteDiseaseUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        user.diseases.remove(*serializer.validated_data['ids'])
        return Response({'message': _('Болезни удалены')}, status=204)