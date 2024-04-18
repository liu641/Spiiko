## Problem
Design a Flask application for a toy shopping website that offers toys, primarily sports-related ones, for kids.

## Solution
### HTML Files
- **index.html**: This is the homepage of the website. It will display a list of all the available toys.
- **product.html**: This page will display the details of a single toy.
- **cart.html**: This page will display the items currently in the user's shopping cart.
- **checkout.html**: This page will allow the user to enter their shipping and payment information and complete the purchase.

### Routes
- **@app.route('/')**: This route will render the homepage (index.html).
- **@app.route('/product/<int:product_id>'**: This route will render the product page (product.html) for the toy with the specified ID.
- **@app.route('/cart')**: This route will render the shopping cart page (cart.html).
- **@app.route('/checkout')**: This route will render the checkout page (checkout.html).
- **@app.route('/add_to_cart')**: This route will add the specified toy to the user's shopping cart.
- **@app.route('/remove_from_cart')**: This route will remove the specified toy from the user's shopping cart.
- **@app.route('/purchase')**: This route will process the user's purchase and complete the checkout process.