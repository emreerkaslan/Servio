from rest_framework import serializers
from .models import Service
from django.utils.timezone import now


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ['pk', 'title', 'description', 'geolocation', 'date', 'giver', 'taker', 'credits', 'recurring',
                  'requests', 'feedbackList', 'tags', 'picture']

        def create(self, validated_data):
            service = Service.objects.create(
                title=validated_data.get("title"),
                description=validated_data.get("description"),
                geolocation=validated_data.get("geolocation"),
                giver=validated_data.get("giver"),
                taker="Default",
                credits=validated_data.get("credits"),
                recurring=False,
                isActive=True,
                tags=validated_data.get("tags"),
                requests=None,
                **validated_data)
            return service

        def update(self, instance, validated_data):
            if instance.isActive and instance.requests.isEmpty:
                for (key, value) in validated_data.items():
                    setattr(instance, key, value)

                instance.save()
            return instance
