from django.db import models

# Create your models here.
class Petani(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    nama = models.CharField(max_length=100)
    luas_tanah = models.IntegerField(default=0)
    
    def __str__(self):
        return self.nama

    class Meta:
        ordering = ['created']
    
class Panenan(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    hasil_panen = models.CharField(max_length=100)
    berat_ton = models.IntegerField(default=0)
    waktu_tanam_hari = models.IntegerField(default=0)
    
    def __str__(self):
        return self.hasil_panen
    
    class Meta:
        ordering = ['created']
    
class Tanaman(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    nama_tanaman = models.CharField(max_length=100)
    jenis = models.CharField(max_length=100)
    waktu_tanam_hari = models.IntegerField(default=0)
    
    def __str__(self):
        return self.nama_tanaman
    class Meta:
        ordering = ['created']