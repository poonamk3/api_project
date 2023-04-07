
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = __all__