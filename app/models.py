from django.db import models

#Add a Support model with name, image
class Support(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='app/static/img/support')

    def __str__(self):
        return self.name

# Add a Game model with title, price, description, image, support(n/n)
class Game(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='app/static/img/game/')
    support = models.ManyToManyField(Support)

    def __str__(self):
        return self.title
