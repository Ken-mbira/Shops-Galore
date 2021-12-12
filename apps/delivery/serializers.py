from rest_framework import serializers,status

from apps.account.models import *
from apps.store.models import *
from apps.delivery.models import *

class RegisterMeansSerializer(serializers.ModelSerializer):
    """This handles the means

    Args:
        serializers ([type]): [description]

    Returns:
        [type]: [description]
    """
    class Meta:
        model = DeliveryMeans
        fields = '__all__'
        read_only_fields = ['owner']

    def save(self,request):
        mean = DeliveryMeans(
            owner = request.user,
            means = self.validated_data['means'],
            image = self.validated_data['image']
        )

        mean.save()
        return mean

class DeliveryMeansImage(serializers.Serializer):
    """This adds a way to update the image for a means

    Args:
        serializers ([type]): [description]
    """
    image = serializers.ImageField(required=True)

    def save(self,means):
        means.image = self.validated_data['image']
        means.save()

class DestinationSerializer(serializers.ModelSerializer):
    """This will handle a destination for a specific location

    Args:
        serializers ([type]): [description]
    """
    class Meta:
        model = Destination
        fields = '__all__'
        read_only_fields = ['means']

    def save(self,means):
        destination = Destination(
            means = means,
            location = self.validated_data['location'],
            price = self.validated_data['price']
        )
        destination.save()
        return destination