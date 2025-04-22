from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from projects.serializers.tags import ListAllTagsSerializer, CreateUpdateTagsSerializer

from projects.models import Tag


# Create your views here.
# К созданным сериализаторам необходимо добавить классовые отображения таким образом,
# чтобы максимально сократить количество эндпоинтов для HTTP методов.

class TagsCreateListAPIView(APIView):
    def get(self, request: Request):
        tags = Tag.objects.all()
        serializer = ListAllTagsSerializer(tags, many=True)
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
            )


    def post(self, request: Request) -> Response:
        serializer = CreateUpdateTagsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

