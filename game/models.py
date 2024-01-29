# game/models.py

from django.db import models
from django.conf import settings

class Character(models.Model):
    name = models.CharField(max_length=100)
    hp = models.IntegerField(default=100)
    atk = models.IntegerField(default=10)
    
    def take_damage(self, damage):
        self.hp -= damage
        self.save()

    def attack(self, enemy):
        enemy.take_damage(self.atk)
        
    class Meta:
        abstract = True

class Protagonist(Character):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Otros atributos específicos del protagonista

class Enemy(Character):
    difficulty = models.IntegerField(default=1)
    # Otros atributos específicos del enemigo

class Achievement(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class ProtagonistAchievement(models.Model):
    protagonist = models.ForeignKey(Protagonist, on_delete=models.CASCADE)
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    date_achieved = models.DateTimeField(auto_now_add=True)


class Level(models.Model):
    level_number = models.IntegerField(unique=True)
    description = models.TextField(blank=True)
    difficulty = models.IntegerField(default=1)
    enemies = models.ManyToManyField(Enemy)

    def __str__(self):
        return f"Level {self.level_number}"
