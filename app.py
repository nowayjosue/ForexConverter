from flask import Flask, render_template, request
from forex import is_valid_currency, convert_currency

app = Flask(__name)

@app.route('/', methods=['GET', 'POST'])
def forex():
    error_message = None
    converted_result = None

    if request.method == 'POST':
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']
        amount = request.form['amount']

        if not is_valid_currency(from_currency) or not is_valid_currency(to_currency):
            error_message = "Invalid currency code."
        elif not amount.replace('.', '', 1).isdigit():
            error_message = "Invalid amount."

        if not error_message:
            converted_result = convert_currency(from_currency, to_currency, amount)

    return render_template('index.html', error_message=error_message, converted_result=converted_result)

if __name__ == '__main__':
    app.run(debug=True)