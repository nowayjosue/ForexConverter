import requests

def is_valid_currency(currency_code):
    # You can implement currency code validation here
    # Return True if valid, False if not
    return True

def convert_currency(from_currency, to_currency, amount):
    # Make an API request to get exchange rates
    base_url = 'https://api.apilayer.com/exchangerates_data/latest'
    api_key = 'your_api_key_here'  # Replace with your API key from exchangerate.host
    params = {'base': from_currency, 'symbols': to_currency}
    headers = {'apikey': api_key}

    response = requests.get(base_url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        conversion_rate = data['rates'][to_currency]
        converted_amount = round(float(amount) * conversion_rate, 2)
        return converted_amount
    else:
        return None