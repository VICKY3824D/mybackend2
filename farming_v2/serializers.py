from rest_framework import serializers
from farming_v2.models import Petani, Panenan, Tanaman

class PetaniSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(max_length=100)
    # password = serializers.CharField(max_length=100)
    # nama = serializers.CharField(max_length=100)
    # luas_tanah = serializers.IntegerField(default=0)
    
    # def create(self, validated_data):
    #     """
    #     Create and return a new `Snippet` instance, given the validated data.
    #     """
    #     return Petani.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.username = validated_data.get('username', instance.username)
    #     instance.password = validated_data.get('password', instance.password)
    #     instance.nama = validated_data.get('nama', instance.nama)
    #     instance.luas_tanah = validated_data.get('luas_tanah', instance.luas_tanah)
    #     instance.save()
    #     return instance
    
    class Meta:
        model = Petani
        fields = ('id', 'username','password','nama', 'luas_tanah')
        
class PanenanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Panenan
        fields = ['id', 'hasil_panen', 'berat_ton', 'waktu_tanam_hari']
        
class TanamanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tanaman
        fields = ['id', 'nama_tanaman', 'jenis', 'waktu_tanam_hari']
        