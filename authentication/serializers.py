from .models import User
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField


class UserCreationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=25)
    email = serializers.EmailField(max_length=80)
    phone_number = PhoneNumberField(allow_null=False, allow_blank=True)
    password = serializers.CharField(min_length=8)

    class Meta:
        model = User
        fields = ["username", "email", "phone_number", "password"]

    
    def validate(self, attrs):
        username_exists = User.objects.filter(username=attrs["username"]).exists()
        if username_exists:
            raise serializers.ValidationError(detail="User with Username exits")
        
        email_exists = User.objects.filter(username=attrs["email"]).exists()
        if email_exists:
            raise serializers.ValidationError(detail="User with Email exits")
        
        phone_number_exists = User.objects.filter(username=attrs["phone_number"]).exists()
        if phone_number_exists:
            raise serializers.ValidationError(detail="User with Phone_number exits")

        return super().validate(attrs)
    
