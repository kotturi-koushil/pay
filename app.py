import razorpay
from flask import Flask, render_template, request
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

    # Replace with your actual key_id and key_secret
key_id = os.getenv("RAZORPAY_KEY_ID")
key_secret = os.getenv("RAZORPAY_KEY_SECRET")

client = razorpay.Client(auth=(key_id, key_secret))

@app.route('/', methods=['GET', 'POST'])
def index():
        if request.method == 'POST':
            amount = int(request.form['amount']) * 100  # Amount in paise
            currency = "INR"
            receipt = "order_rcptid_11"

            # Create an order
            order_data = {
                "amount": amount,
                "currency": currency,
                "receipt": receipt,
                "payment_capture": 1  # Auto capture
            }
            order = client.order.create(data=order_data)
            order_id = order['id']

            return render_template('index.html', key_id=key_id, amount=amount, currency=currency, order_id=order_id)
        return render_template('index.html', key_id=key_id)

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=10000)
