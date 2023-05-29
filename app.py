from flask import Flask, jsonify

import random

import string

app = Flask(__name__)

@app.route('/visa', methods=['GET'])

def generate_visa():

    visa_prefix = "4"

    for i in range(0, 5):

        visa_prefix += str(random.randint(0, 9))

    card_number = visa_prefix + ''.join(random.choice(string.digits) for i in range(10))

    check_digit = generate_check_digit(card_number)

    expiration_month = str(random.randint(1, 12)).zfill(2)

    expiration_year = str(random.randint(2023, 2030))

    cvv = ''.join(random.choice(string.digits) for i in range(3))

    return jsonify({

        "card": card_number + str(check_digit),

        "date": expiration_month + "/" + expiration_year,

        "cvv": cvv,

        "card_info": card_number + "|" + expiration_month + "|" + expiration_year + "|" + cvv

    })

def generate_check_digit(card_number):

    digits = [int(x) for x in str(card_number)]

    for i in range(len(digits) - 2, -1, -2):

        digits[i] *= 2

        if digits[i] > 9:

            digits[i] -= 9

    total = sum(digits)

    return (10 - total % 10) % 10

if __name__ == '__main__':

    app.run(debug=True)

