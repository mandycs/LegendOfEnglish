# game/serializers.py

from rest_framework import serializers
from .models import Protagonist, Enemy, Achievement, Level

class ProtagonistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Protagonist
        fields = '__all__'

class EnemySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enemy
        fields = '__all__'

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'
