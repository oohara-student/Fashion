from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField('服ジャンル',max_length=100)

    def __str__(self):
        return '<' + self.name +  '>'
    

class Kinds(models.Model):
    name = models.CharField('服種類',max_length=100)

    def __str__(self):
        return '<'  + self.name +  '>'

class Clothes(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    kinds = models.ForeignKey(Kinds, on_delete=models.CASCADE)
    size  = models.IntegerField('サイズ',default=0)
    pattern = models.BooleanField('柄')
    color = models.DecimalField('服カラー',default=0, max_digits=3, decimal_places=1,)
    image = models.ImageField('画像',upload_to='images',blank=None, null=True)
    def __str__(self):
        return '<id:' + str(self.id)  +  '>'