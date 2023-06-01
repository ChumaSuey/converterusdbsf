import requests
from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.


def index(request: HttpRequest):
    context = {
        "dolar_price": "", "dollars": "",
        "bolivares": "", "bolivares_price": ""
    }
    if request.method == "POST":
        try:
            dollars = float(request.POST.get('dolar', 0))
            bolivares = float(request.POST.get('bolivares', 0))
        except:
            dollars = 0
            bolivares = 0
        response = requests.get(
            "https://s3.amazonaws.com/dolartoday/data.json"
        )
        dolar_price = response.json()['USD']['dolartoday']
        if dollars:
            context["dolar_price"] = str(float(dolar_price) * dollars)
            context["dollars"] = str(dollars)
        if bolivares:
            context["bolivares_price"] = str(bolivares / float(dolar_price))
            context["bolivares"] = str(bolivares)


    template = 'index.html'
    return render(request=request, template_name=template, context=context)

# eee

# context["bolivares"] = bolivares
# context["bolivares"] = bolivares / float(dolar_price)

# def currency():
    #   """ Data de Dolartoday  """
  #  module_dir = os.path.dirname(__file__)  # get current directory
   # file_path = os.path.join(module_dir, 'currencies.json')
    # with open(file_path, "r") as f:
    #   currency_data = json.loads(f.read())
    # return currency_data
