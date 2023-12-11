from Users.models import UserProfile
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'phone', 'telegram_pk')

    def create(self, validated_data):
        return UserProfile.objects.create_user(**validated_data)