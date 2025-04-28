from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from projects.models import Tag


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


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
        fields = '__all__'

    def validate_name(self, value: str=None) -> str:
        if not value:
            raise serializers.ValidationError(
                'This field is required.'
            )

        if not isinstance(value, str):
            raise serializers.ValidationError(
                'This field must be a valid string.'
            )

        if len(value) < 2:
            raise serializers.ValidationError(
                'The length of this field must be at least 2 characters.'
            )

        return value

    def create(self, validated_data: dict[str, str | int]) -> Tag:
        tag_name_exists = Tag.objects.filter(
            name=validated_data['name']
        ).exists()

        if tag_name_exists:
            raise serializers.ValidationError(
                "Tag with this name already created."
            )

        return Tag.objects.create(**validated_data)

    def update(self, instance: Tag, validated_data: dict[str, str | int]) -> Tag:
        tag_name_exists = Tag.objects.exclude(id=instance.pk).filter(
            name=validated_data['name']
        ).exists()

        if tag_name_exists:
            raise serializers.ValidationError(
                "Tag with this name already created."
            )

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        return instance
