from rest_framework import serializers

from .models import Topic, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id',
            'poster',
            'comment',
            'topic'
        )

    topic = serializers.PrimaryKeyRelatedField(queryset=Topic.objects.all())

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = (
            'id',
            'poster',
            'title',
            'description',
            'comments'
        )
    comments = CommentSerializer(many=True, read_only=True)

class TopicFlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = (
            'id',
            'title',
        )