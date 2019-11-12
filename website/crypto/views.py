from django.shortcuts import render

# Create your views here.
def home(request):
	import requests
	import json
	#grap price data
	price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,LTC,TRX,ADA,XMR,DASH&tsyms=USD")
	price = json.loads(price_request.content)
	#grab the news
	api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
	api = json.loads(api_request.content)
	return render(request,'home.html', {'api' : api,'price':price})


def prices(request):
	if request.method == 'POST':
		quote = request.POST['quote']
		return render(request,'prices.html', {'quote':quote}),
	else:	
		return render(request,'prices.html', {})


