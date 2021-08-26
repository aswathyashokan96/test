from django.db import models

# Create your models here. 

class Course(models.Model):
    name = models.CharField(max_length=50)
    # description = models.CharField(max_length=1000)
    # image = models.ImageField()
    def __str__(self):
        return self.name
    


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    image = models.ImageField()


class Workshop(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    image = models.ImageField()


class Feedback(models.Model):
    name = models.CharField(max_length=50)
    feedback = models.CharField(max_length=1000)
    image = models.ImageField()


class Callme(models.Model):
    name1 = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    interested = models.CharField(max_length=50, null=True, blank=True)

    # def __str__(self):
    #     return self.name1

class Contact(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField(max_length=2000, null=True, blank=True)

    # def __str__(self):
    #     return self.name


# class details(models.Model):
#     course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True,blank=True)

#     def __str__(self):
#         return self.course
    
class Photos(models.Model):
    name = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()
    overview = models.CharField(max_length=2000, null=True)

    def __str__(self):
        return self.description



class About(models.Model):
    about = models.TextField(null=True)
    # image = models.ImageField(null=True)


class Carousal(models.Model):
    image = models.ImageField()
#     desc = models.CharField(max_length=50, null=True)



class Registerfirst(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)

   

   