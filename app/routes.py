from flask import Blueprint, render_template, request, jsonify
import stripe
from .config import Config

main = Blueprint('main', __name__)

stripe.api_key = Config.STRIPE_SECRET_KEY

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/process_cards', methods=['POST'])
def process_cards():
    cards_data = request.form['cards']
    cards = cards_data.split('\n')
    results = []

    for card in cards:
        card_info = card.split('|')
        if len(card_info) == 4:
            number, exp_month, exp_year, cvc = card_info
            try:
                token = stripe.Token.create(
                    card={
                        "number": number,
                        "exp_month": exp_month,
                        "exp_year": exp_year,
                        "cvc": cvc,
                    },
                )
                results.append(f"Tarjeta {number[-4:]}: Token creada con éxito")
            except stripe.error.StripeError as e:
                results.append(f"Tarjeta {number[-4:]}: Error al crear el token - {e.user_message}")
        else:
            results.append(f"Formato inválido: {card}")

    return jsonify(results)
