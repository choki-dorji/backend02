from rest_framework import serializers
from .models import  User, Marriage, ChildData
# #shorter way
# class ReviewSerializer(serializers.ModelSerializer):
#     review_user = serializers.StringRelatedField(read_only=True)
#     class Meta:
#         model = Review
#         # fields = '__all__'
#         exclude = ('Watchlist',)



# class WatchlistSerializer(serializers.ModelSerializer):
#     # reviews = ReviewSerializer(many =True, read_only=True)
#     # len_name = serializers.SerializerMethodField()
#     platform = serializers.CharField(source='platform.name')
#     class Meta:
#         model = Watchlist
#         fields = "__all__"
        # field = ['id', 'name', 'description']
        # exclude = ['active']
        
    # def get_len_name(self, object):
    #     return len(object.name)

# class StreamPlatformsSerializer(serializers.ModelSerializer):
#     watchlist = WatchlistSerializer(many=True, read_only=True)
#     # watchlist = serializers.StringRelatedField(many=True)
#     # watchlist = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='movie_main')
#     class Meta:
#         model = StreamPlatforms
#         fields = "__all__"   

#serializer with long way to serialize
# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError('Name must be at least 2 characters')
#     else:
#         return value

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Movies.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

    # #object level validation
    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("The name and description cannot be the same")
    #     else:
    #         return data
    
    #field level validation
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError('Name must be at least 2 characters')
    #     else:
    #         return value

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        exclude = ('status', 'user', )

class MarriageSerializer(serializers.ModelSerializer):
    CID = serializers.ReadOnlyField(source='YOUR_CId.CID')
    Name = serializers.ReadOnlyField(source='YOUR_CId.Name')
    Gender = serializers.ReadOnlyField(source='YOUR_CId.Gender')
    village = serializers.ReadOnlyField(source='YOUR_CId.Village')
    chiwog = serializers.ReadOnlyField(source='YOUR_CId.Chiwog')
    contact = serializers.ReadOnlyField(source='YOUR_CId.contact_number')
    Email = serializers.ReadOnlyField(source='YOUR_CId.email')

    Spouse_name = serializers.ReadOnlyField(source='Spouce_ID.Name')
    Spouse_gender = serializers.ReadOnlyField(source='Spouce_ID.Gender')
    Spouse_contact = serializers.ReadOnlyField(source='Spouce_ID.contact_number')
    # female = FemaleUserDataSerializer
    class Meta:
        model = Marriage
        # fields = '__all__'
        exclude = ('status',)

    # def validate(self, data):
    #     if data['YOUR_CId.CID'] == data['Spouce_ID.CID']:
    #         raise serializers.ValidationError("HOW CAN U MARRY YOUR SELF")
    #     else:
    #         return data
    def save(self):
        password = self.validated_data['Your_CID']
        password2 = self.validated_data['Spouce_ID']
        if password == password2:
            raise serializers.ValidationError({'errer':'cid should be different'})
        # if User.objects.filter(email=self.validated_data['email']).exists():
        #     raise serializers.ValidationError({'errer':'email already in use'})
            
        account = User(email=self.validated_data['email'], 
                username=self.validated_data['username'], 
                CID=self.validated_data['YOUR_CId'], 
                spouse_cid = self.validated_data['Spouce_ID'],
                Marriage_certificate =  self.validated_data['Marriage_certificate'],
                status = self.validated_data['status']
        )
        account.set_password(password)
        account.save()
        return account


class ChildDataSerializer(serializers.ModelSerializer):
    Fathers_name = serializers.ReadOnlyField(source='Marriage_ID.Name')
    Fathers_CID = serializers.ReadOnlyField(source='Marriage_ID.CID')
    Fathers_Contact = serializers.ReadOnlyField(source='Marriage_ID.contact_number')

    Mothers_name = serializers.ReadOnlyField(source='Marriage_ID.Spouse_name')
    Mothers_CID = serializers.ReadOnlyField(source='Marriage_ID.Spouce_ID')
    Mothers_contact = serializers.ReadOnlyField(source='Marriage_ID.Spouse_contact')
    class Meta:
        model = ChildData
        fields = '__all__'