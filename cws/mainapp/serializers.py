from rest_framework import serializers
from mainapp.models import ContentCard, Comment


class ContentCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentCard
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


