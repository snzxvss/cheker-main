# Stripe Integration with Flask

This project demonstrates a simple integration of Stripe payment processing with a Flask web application. It allows users to input credit card information, which is then processed using Stripe's API to create tokens for transactions.

## Features

- Flask web application with a simple UI for entering credit card details.
- Stripe API integration for processing credit card information.
- Secure handling of sensitive information using environment variables.

## Getting Started

### Prerequisites

- Python 3.6+
- pip

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/snzxvss/cheker-main.git
2. Navigate to the project directory:
    ```sh
    cd flask-stripe-project
3. Install the required packages:
    ```sh
    pip install -r requirements.txt
4. Set up the environment variables. Create a .env file in the app directory and add the following:
    ```sh
    SECRET_KEY=your_secret_key
    STRIPE_SECRET_KEY=your_stripe_secret_key
    STRIPE_PUBLISHABLE_KEY=your_stripe_publishable_key

Replace your_secret_key, your_stripe_secret_key, and your_stripe_publishable_key with your actual keys.

## Running the Application

Start the Flask application:
    ```sh
    python run.py

Open a web browser and navigate to http://127.0.0.1:5000/ to see the application in action.
Usage

Enter credit card details in the format Number|MM|YYYY|CVC in the text area provided on the homepage and submit the form to process the cards through Stripe.

Contributing
Contributions are welcome! Please feel free to submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.