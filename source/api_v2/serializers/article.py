from rest_framework import serializers

from webapp.models.article import Article


class ArticleSerializer(serializers.ModelSerializer):
    test_id = serializers.IntegerField(write_only=True)


    def validate(self, attrs):
        return super().validate(attrs)

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Длина додлжна быть больше пяти")
        return value

    class Meta:
        model = Article
        fields = ["id", "title", "content", "status", "tags", "created_at", "updated_at", "author", "test_id"]
        read_only_fields = ["id", "created_at", "updated_at", "author"]

    def create(self, validated_data):
        test_id = validated_data.pop("test_id")
        print(test_id)
        return super().create(validated_data)
