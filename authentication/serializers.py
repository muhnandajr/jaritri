from rest_framework import serializers
from authentication.models import User, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserProfile
        fields = ('nim', 'dob','number_phone', 'village','rt_village','rw_village', 'province', 'city', 'postal_code', 'photo')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('url', 'email', 'first_name', 'last_name', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()

        profile.nim = profile_data.get('nim', profile.nim)
        profile.dob = profile_data.get('dob', profile.dob)
        profile.number_phone = profile_data.get('number_phone', profile.number_phone)
        profile.village = profile_data.get('village', profile.village)
        profile.rt_village = profile_data.get('rt_village', profile.rt_village)
        profile.rw_village = profile_data.get('rw_village', profile.rw_village)
        profile.province = profile_data.get('province', profile.province)
        profile.city = profile_data.get('city', profile.city)
        profile.postal_code = profile_data.get('postal_code', profile.postal_code)
        profile.photo = profile_data.get('photo', profile.photo)
        profile.save()

        return instance