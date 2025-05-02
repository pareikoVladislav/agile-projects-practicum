from django.db.models import QuerySet
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from projects.serializers.tags import TagsSerializer, CreateUpdateTagsSerializer
from projects.models import Tag


class TagsListCreateAPIView(APIView):
    def get_objects(self) -> QuerySet:
        return Tag.objects.all()

    def get(self, request: Request, *args, **kwargs) -> Response:
        tags = self.get_objects()

        if not tags.exists():
            return Response(
                data=[],
                status=status.HTTP_204_NO_CONTENT
            )

        serializer = TagsSerializer(tags, many=True)

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

    def post(self, request: Request, *args, **kwargs) -> Response:
        """
        {
            "name": "HR"
        }
        """
        serializer = CreateUpdateTagsSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            data=serializer.data,
            status=status.HTTP_201_CREATED
        )


class TagsRetrieveUpdateDeleteAPIView(APIView):
    def get_object(self, pk: int) -> Tag:
        return get_object_or_404(Tag, pk=pk)

    def get(self, request: Request, *args, **kwargs) -> Response:
        tag = self.get_object(pk=kwargs['pk'])

        serializer = TagsSerializer(tag)

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

    def put(self, request: Request, *args, **kwargs) -> Response:
        tag = self.get_object(pk=kwargs['pk'])

        serializer = CreateUpdateTagsSerializer(instance=tag, data=request.data)

        if not serializer.is_valid():
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer.save()

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

    def delete(self, request: Request, *args, **kwargs) -> Response:
        tag = self.get_object(pk=kwargs['pk'])

        tag.delete()

        return Response(
            data={"message": "Tag was deleted successfully."},
            status=status.HTTP_204_NO_CONTENT
        )
