from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

class Comment(models.Model):
    post = models.ForeignKey(Board, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=10)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class Comment2(models.Model):
    post = models.ForeignKey(Board, related_name='comments2', on_delete=models.CASCADE)
    author = models.CharField(max_length=10)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text