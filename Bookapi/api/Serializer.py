from rest_framework import serializers
from .models import*




# create serializers here

class BookSrrializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'  # all fields in the model
