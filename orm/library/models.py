from django.db import models
 
# Create your models here.
class Kitob(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()


    def __str__(self):
        return f"{self.id} - {self.name}"
    

# class Kitobxon(models.Model):
#     name = models.CharField(max_length=150)
#     #age = models.CharField(max_length=100)
#     description = models.TextField()

#     # def __str__(self):
#     #     return f"{self.id}" - {self.name}
     