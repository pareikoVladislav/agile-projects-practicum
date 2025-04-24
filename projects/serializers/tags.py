from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from projects.models import Tag

# Необходимо создать новые сериализаторы, которые помогут получать информацию обо всех тегах,
# а так же создавать \ обновлять тег.

class ListAllTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class CreateUpdateTagsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=20,
        min_length=2,
        required=True,
        validators=[
            UniqueValidator(
                queryset=Tag.objects.all(),
                message="Error. Тэг с таким именем существует"
            )
        ]
    )

    class Meta:
        model = Tag
        fields = "__all__"


