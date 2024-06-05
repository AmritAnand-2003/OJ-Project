from django.db import models

# Create your models here.

DIFFICULTY_CHOICES = [
    ("Easy", "Easy"),
    ("Medium", "Medium"),
    ("Hard", "Hard"),
]

class Problem(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    difficulty = models.CharField(
        max_length=10,
        blank=True,
        choices=DIFFICULTY_CHOICES,
    )
    def __str__(self):
        return f"{self.id}"
    
class Submission(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    language = models.CharField(max_length=100)
    code = models.TextField()
    verdict = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

class RunCode(models.Model):
    language = models.CharField(max_length=100)
    code = models.TextField()
    input_data = models.TextField(null=True, blank=True)
    output_data = models.TextField(null=True, blank=True)


class TestCases(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    input_data = models.TextField(null=True, blank=True)
    output_data = models.TextField(null=True, blank=True)