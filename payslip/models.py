from django.db import models

# Create your models here.

class Grade(models.Model):
    positon = models.CharField(max_length=250)
    basic_salary = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.positon
    class Meta:
        verbose_name_plural = "Grade"

class staff(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField()
    hour = models.PositiveIntegerField(default=0)
    gross_salary = models.PositiveIntegerField(default=0)
    grade_status = models.ForeignKey(Grade, on_delete=models.CASCADE)

    def save(self, *args,**kwargs):
        self.gross_salary = (self.hour * self.grade_status.basic_salary)
        return super().save(*args,**kwargs)
    

    def __str__(self):
        return self.first_name
        
    class Meta:
        verbose_name_plural = "Staff"
        ###