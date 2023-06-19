from django.db import models
import barcode
from  barcode.writer import ImageWriter
from io  import BytesIO
from django.core.files import File
# Create your models here.
class Product(models.Model):
    name= models.CharField(max_length=200)
    barcode=models.ImageField(upload_to='images/', blank=True)
    def __str__(self):
        return str(self.name)
    
    def save(self, *args, **kwargs):
        EAN = barcode.get_barcode_class('ean13')
        ean = EAN('5901234123457', writer= ImageWriter())
        buffer= BytesIO()
        ean.write(buffer)
        self.barcode.save('barcode.png', File(buffer), save=False)
        return super().save(*args, **kwargs)
