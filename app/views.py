from django.shortcuts import render

def home(request):
    import requests
    import json

    price_request = requests.get(
        'https://blockchain.info/ticker')
    price = json.loads(price_request.content)

    price2_request = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false')

    price2 = json.loads(price2_request.content)


    #informacje
    api_request = requests.get('https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=6edc45b576a54bce872904f138814980')
    api = json.loads(api_request.content)
    return render(request, 'home.html', {'api': api, 'price' : price, 'price2' : price2})


def prices(request):
    return render(request, 'prices.html', {})