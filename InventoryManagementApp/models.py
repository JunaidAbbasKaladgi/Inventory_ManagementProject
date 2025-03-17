from django.db import models

# class productTable(models.Model):
#             Name=models.CharField(max_length=20,null=False,blank=False)
#             desc=models.TextField(null=False,blank=False)
#             price=models.DecimalField(max_digits=19,decimal_places=2,null=False,blank=False)
#             quantity=models.IntegerField(null=False,blank=False)

            
class CategoryTable(models.Model):
            Category=models.CharField(max_length=20,null=False,blank=False)            

class CustomerTable(models.Model):
            c_name = models.CharField(max_length=255)
            c_address = models.TextField()
            c_email = models.EmailField(unique=True)
            c_phone = models.CharField(max_length=15, unique=True)

class SupplierTable(models.Model):
            s_name = models.CharField(max_length=255)
            s_address = models.TextField()
            s_email = models.EmailField(unique=True)
            s_phone = models.CharField(max_length=15, unique=True)            

            def __str__(self):
                    return self.Name