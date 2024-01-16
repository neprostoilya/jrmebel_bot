from rest_framework import serializers

from Users.models import UserProfile
from config.settings import BOT_PK
from .logics.login import authenticate


class UserSerializer(serializers.ModelSerializer):
    """
    Get Users
    """
    class Meta:
        model = UserProfile
        fields = ('pk', 'username', 'phone', 'telegram_pk',)

class RegistrationSerializer(serializers.ModelSerializer):
    """
    Registration User
    """
    token = serializers.CharField(
        read_only=True
    )
    username = serializers.CharField()
    phone = serializers.CharField(
        min_length=6,
        max_length=13,
    )
    telegram_pk = serializers.CharField(
        max_length=20, 
    )

    def create(self, validated_data):
        username = validated_data['username']
        phone = validated_data['phone']
        telegram_pk = validated_data['telegram_pk']
        
        user = UserProfile.objects.create_user(
            username=username,
            phone=phone,
            telegram_pk=telegram_pk
        )
        return user
        
    class Meta:
        model = UserProfile
        fields = ('username', 'phone', 'telegram_pk', 'token')

class LoginSerializer(serializers.Serializer):
    """
    Login User
    """
    telegram_pk = serializers.CharField(
        max_length=20, 
    )
    token = serializers.CharField(
        read_only=True
    )

    def validate(self, attrs):
        telegram_pk = attrs.get('telegram_pk')
        if telegram_pk is not None:
            user = authenticate(
                telegram_pk=telegram_pk
            )

            if user is not None:
                return {
                    'phone': user.phone,
                    'username': user.username,
                    'token': user.token
                }
            raise serializers.ValidationError('User Not Found')
        raise serializers.ValidationError('You didnt fill in the field')
