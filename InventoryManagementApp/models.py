from django.db import models

class productTable(models.Model):
            Name=models.CharField(max_length=20,null=False,blank=False)
            desc=models.TextField(null=False,blank=False)
            price=models.DecimalField(max_digits=19,decimal_places=2,null=False,blank=False)
            quantity=models.IntegerField(null=False,blank=False)

            def __str__(self):
                    return self.Name
