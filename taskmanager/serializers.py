from rest_framework import serializers
from taskmanager.models import Task


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'account', 'team', 'created_at', 'title',
                  'content', 'status','progression','due_date','is_repeatable', 'repeat_every', 'repeat_count',
                  'is_event','is_prostpondable','is_referable','tags',
                  )
        read_only_fields = ('created_at',)

    def create(self, validated_data):
        del validated_data['tags']
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.account = validated_data.get('account', instance.account)
        instance.team = validated_data.get('team', instance.team)
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.status = validated_data.get('status', instance.status)
        instance.progression = validated_data.get('progression', instance.progression)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.is_repeatable = validated_data.get('is_repeatable', instance.is_repeatable)
        instance.repeat_every = validated_data.get('repeat_every', instance.repeat_every)
        instance.repeat_count = validated_data.get('repeat_count', instance.repeat_count)
        instance.is_event = validated_data.get('is_event', instance.is_event)
        instance.is_prostpondable = validated_data.get('is_prostpondable', instance.is_prostpondable)
        instance.is_referable = validated_data.get('is_referable', instance.is_referable)
        instance.tags = validated_data.get('tags', instance.tags)
        instance.save()
        
        return instance
