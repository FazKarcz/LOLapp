import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


# Klasa reprezentująca widok API dla regionu Ameryki
class AmericanApiView(APIView):
    # Ustawienia autentykacji i uprawnień dla tego widoku
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        # Adres URL API dla rankingu w regionie Ameryki
        api_url = 'https://americas.api.riotgames.com/lor/ranked/v1/leaderboards'
        # Klucz API do autoryzacji z serwisem Riot Games
        api_key = 'RGAPI-07e7a1c5-47d7-424c-86e6-205768bc4281'
        try:
            # Wysłanie żądania GET do API z uwzględnieniem klucza API
            response = requests.get(api_url, params={'api_key': api_key})
            response.raise_for_status()
            data = response.json()
            return Response(data)
        except requests.exceptions.RequestException as e:
            return Response({'error': str(e)}, status=500)


class EuropeApiView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):

        api_url = 'https://europe.api.riotgames.com/lor/ranked/v1/leaderboards'

        api_key = 'RGAPI-07e7a1c5-47d7-424c-86e6-205768bc4281'
        try:

            response = requests.get(api_url, params={'api_key': api_key})
            response.raise_for_status()
            data = response.json()
            return Response(data)
        except requests.exceptions.RequestException as e:

            return Response({'error': str(e)}, status=500)


# Klasa reprezentująca widok API dla innych regionów (np. Azja, Oceania)
class OtherApiView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):

        api_url = 'https://sea.api.riotgames.com/lor/ranked/v1/leaderboards'

        api_key = 'RGAPI-07e7a1c5-47d7-424c-86e6-205768bc4281'
        try:

            response = requests.get(api_url, params={'api_key': api_key})
            response.raise_for_status()
            data = response.json()
            return Response(data)
        except requests.exceptions.RequestException as e:

            return Response({'error': str(e)}, status=500)
