from random import randint


# w settings.py w TEMPLATES sa kontekst procesory ktore automatycznie sa zawsze w kontekscie przekazywanym do widkow nawet jak nie odajemy kontekstu
# mozemy dopisac tam wlasne pliki z finkcjiami ktore zawsze bedą przekazywane do kontekstu, jak np tutaj w apce films, ale uwazajmy by nienadpisac czegos

def random_number(request):
    result = randint(1,10)
    if result == 10:
        return {'result': result, 'message': 'Wygrałeś!'}
    else:
        return  {'result': result}
