from rest_framework import serializers

from webapp.models import Tag
from webapp.models.article import statuses, Article


class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=50, required=True)
    text = serializers.CharField(required=True, source="content")
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    status = serializers.ChoiceField(choices=statuses, default=statuses[0][0])
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all(), required=False)

    def validate(self, attrs):
        return super().validate(attrs)

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Длина додлжна быть больше пяти")
        return value


    def create(self, validated_data):
        tags = validated_data.pop('tags', [])
        article = Article.objects.create(**validated_data)
        article.tags.set(tags)
        return article

    def update(self, instance, validated_data):
        tags = validated_data.pop('tags', [])
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        instance.tags.set(tags)
        return instance