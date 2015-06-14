from currencies.models import Currency


def currencies(request):
    currencies = Currency.objects.active()

    if request.session.get('currency'):
        currency = Currency.objects.get(id=request.session['currency'])

    else:
        try:
            currency = Currency.objects.get(is_default__exact=True)
        except Currency.DoesNotExist:
            currency = None
        request.session['currency'] = currency

    return {
        'CURRENCIES': currencies,
        'CURRENCY': currency
    }
