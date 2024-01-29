from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Protagonist, Enemy, Achievement, Level
from .serializers import ProtagonistSerializer, EnemySerializer, AchievementSerializer, LevelSerializer
import requests

class ProtagonistListCreateView(generics.ListCreateAPIView):
    queryset = Protagonist.objects.all()
    serializer_class = ProtagonistSerializer

class EnemyListCreateView(generics.ListCreateAPIView):
    queryset = Enemy.objects.all()
    serializer_class = EnemySerializer

class AchievementListCreateView(generics.ListCreateAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

class LevelListCreateView(generics.ListCreateAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class CombatView(APIView):
    def post(self, request, *args, **kwargs):
        protagonist_id = request.data.get('protagonist_id')
        enemy_id = request.data.get('enemy_id')
        spell_text = request.data.get('spell_text')  # Texto del hechizo

        # Encuentra el protagonista y el enemigo basado en los ID proporcionados
        protagonist = Protagonist.objects.get(id=protagonist_id)
        enemy = Enemy.objects.get(id=enemy_id)

        # Realiza una solicitud HTTP a la aplicación de análisis de texto
        analysis_response = requests.post('http://localhost:8000/analyze_text/', data={'spell_text': spell_text})

        if protagonist and enemy:
            if analysis_response.status_code == 200:
                # El análisis fue exitoso
                spell_success = analysis_response.json()['spell_success']

                if spell_success:
                    # El hechizo tiene éxito, no haces daño al protagonista
                    result_message = "El hechizo tiene éxito."
                    enemy.take_damage(protagonist.atk)
                else:
                    # El hechizo falla, le haces daño al protagonista
                    protagonist.take_damage(enemy.atk)
                    result_message = "El hechizo falla y el protagonista recibe daño."

                # Aquí va la lógica adicional del combate

                return Response({
                    "enemy": EnemySerializer.data,
                    "protagonist": ProtagonistSerializer.data,
                    "result_message": result_message
                })
            else:
                # El análisis de texto falló
                return Response({"message": "El análisis de texto falló"}, status=400)

        return Response({"message": "Combate no válido"}, status=400)
# Puedes añadir más vistas según sea necesario, por ejemplo, para actualizar o eliminar.
