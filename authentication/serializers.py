from .models import User
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField

class UserCreationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=50)
    phone_number = PhoneNumberField(allow_null=False,allow_blank=False)
    password = serializers.CharField(min_length=8)

    class Meta:
        model = User
        fields = ['username','email','phone_number','password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self,attrs):
        super().validate(attrs)
        username_exists = User.objects.filter(username=attrs['username']).exists()

        if username_exists:
            raise serializers.ValidationError("User with name exists")

        email_exists = User.objects.filter(email =attrs['email']).exists()

        if email_exists:
            raise serializers.ValidationError("Email already exists")

        phone_number_exists = User.objects.filter(phone_number =attrs['phone_number']).exists()

        if phone_number_exists:
            raise serializers.ValidationError("Phone Number already exists")

        return attrs

