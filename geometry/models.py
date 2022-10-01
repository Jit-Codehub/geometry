from django.db import models

class degtorad(models.Model):
    input=models.CharField(max_length=500)
    result=models.CharField(max_length=500)
    detailSteps=models.TextField()
    url=models.CharField(max_length=200)        
    date_modified = models.DateTimeField(null=True)

    def __str__(self):
        return self.input

class radtodeg(models.Model):
    input=models.CharField(max_length=500)
    result=models.CharField(max_length=500)
    detailSteps=models.TextField()
    url=models.CharField(max_length=200)        
    date_modified = models.DateTimeField(null=True)

    def __str__(self):
        return self.input

class supplementary(models.Model):
    input=models.CharField(max_length=100)
    input_type = models.CharField(max_length=100)
    result=models.CharField(max_length=500)
    detailSteps=models.TextField()
    url=models.CharField(max_length=200)        
    date_modified = models.DateTimeField(null=True)

    def __str__(self):
        return self.input


class complementary(models.Model):
    input=models.CharField(max_length=100)
    input_type = models.CharField(max_length=100)
    result=models.CharField(max_length=500)
    detailSteps=models.TextField()
    url=models.CharField(max_length=200)        
    date_modified = models.DateTimeField(null=True)

    def __str__(self):
        return self.input

class reflex(models.Model):
    input=models.CharField(max_length=100)
    input_type = models.CharField(max_length=100)
    result=models.CharField(max_length=500)
    detailSteps=models.TextField()
    url=models.CharField(max_length=200)        
    date_modified = models.DateTimeField(null=True)

    def __str__(self):
        return self.input
