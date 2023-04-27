from django.shortcuts import render
from django.http import HttpRequest
import requests

# Create your views here.


def index(request: HttpRequest):
    context = {"dolar_price": "", "dollars": "", "bols":""}
    if request.method == "POST":
        dollars = int(request.POST.get('dolar', 0))
        response = requests.get("https://s3.amazonaws.com/dolartoday/data.json")
        dolar_price = response.json()['USD']['dolartoday']
        context["dolar_price"] = float(dolar_price) * dollars
        context["dollars"] = dollars
        context["bols"] = float(dolar_price) / dolar_price
    template = 'index.html'
    return render(request = request, template_name=template, context=context)






#def currency():
 #   """ Data de Dolartoday  """
  #  module_dir = os.path.dirname(__file__)  # get current directory
   # file_path = os.path.join(module_dir, 'currencies.json')
    #with open(file_path, "r") as f:
     #   currency_data = json.loads(f.read())
    # return currency_data

