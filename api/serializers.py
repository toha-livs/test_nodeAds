from rest_framework import serializers

from api.models import Group, Element


class SubGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'group', 'icon', 'name', 'description')


class FilteredListSerializer(serializers.ListSerializer):

    def to_representation(self, data):
        data = data.filter(moderator_checked=True)
        return super(FilteredListSerializer, self).to_representation(data)


class ElementSerialize(serializers.ModelSerializer):

    date = serializers.DateField(required=False)
    moderator_checked = serializers.NullBooleanField(required=False)

    def create(self, validated_data):
        if 'moderator_checked' in validated_data:
            raise serializers.ValidationError(
                "Unexpected keyword argument 'moderator_check'")
        else:
            element = Element(**validated_data)
            element.save()
            return element

    def update(self, instance, validated_data):
        raise serializers.ValidationError("Method not accepted")

    class Meta:
        model = Element
        list_serializer_class = FilteredListSerializer
        fields = ('id', 'group', 'icon', 'name', 'description', 'date', 'moderator_checked')


class GroupSerialize(serializers.ModelSerializer):

    def get_serialize_groups(self, obj):
        return obj.get_total_groups()

    def get_serialize_element(self, obj):
        return obj.get_total_elements()

    def create(self, validated_data):
        raise serializers.ValidationError("Method not accepted")

    def update(self, instance, validated_data):
        raise serializers.ValidationError("Method not accepted")

    element = ElementSerialize(many=True)
    rel_groups = SubGroupSerializer(many=True)

    total_groups = serializers.SerializerMethodField('get_serialize_groups')
    total_elements = serializers.SerializerMethodField('get_serialize_element')

    class Meta:
        model = Group
        fields = ('id', 'group', 'icon', 'name',
                  'description', 'total_groups',
                  'total_elements', 'element', 'rel_groups',)

