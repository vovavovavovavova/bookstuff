from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from . import models as my_models


class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField()
    password = serializers.CharField(min_length=4, write_only=True)

    class Meta:
        model = my_models.SupportStuff
        fields = ('email', 'username', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class BookSerializer(serializers.ModelSerializer):
    title = serializers.TextField(required=True)
    author = serializers.CharField(min_length=5, max_length=100, required=True)
    language = serializers.CharField(max_length=20)
    buy_price = serializers.FloatField()
    sell_price = serializers.FloatField()

    class Meta:
        model = my_models.Book
        fileds = ('title', 'author', 'language', 'buy_price', 'sell_price')
        exclude = tuple()


    def create(self, validated_data):
        #print('validated_data:', validated_data)
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance


class OfferSerializer(serializers.ModelSerializer):
    title = serializers.TextField(max_length=50, required=True)
    data = serializers.serializers.JSONField()
    book_id = serializers.RelatedField(read_only=True)

    class Meta:
        model = my_models.Offer
        fields = ('title', 'data', 'book_id')
        exclude = tuple()


    def create(self, validated_data):
        
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance


class OfferResolveSerializer(serializers.ModelSerializer):
    status = serializers.TextField(required=True)
    offer_id = serializers.RelatedField(read_only=True)
    support_stuff_id = serializers.RelatedField(read_only=True)

    class Meta:
        model = my_models.OfferResolve
        fields = ('status', 'offer_id', 'support_stuff_id')
        exclude = tuple()


    def create(self, validated_data):
        
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance
