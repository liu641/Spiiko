
# Import necessary modules
from flask import Flask, render_template, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy

# Create a Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///toys.db'
db = SQLAlchemy(app)

# Define the Toy model
class Toy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120))
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(120))

# Define the Cart model
class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    toy_id = db.Column(db.Integer, db.ForeignKey('toy.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# Create the database tables
db.create_all()

# Define the home route
@app.route('/')
def home():
    toys = Toy.query.all()
    return render_template('index.html', toys=toys)

# Define the product route
@app.route('/product/<int:product_id>')
def product(product_id):
    toy = Toy.query.get(product_id)
    return render_template('product.html', toy=toy)

# Define the cart route
@app.route('/cart')
def cart():
    cart_items = CartItem.query.filter_by(user_id=session['user_id']).all()
    return render_template('cart.html', cart_items=cart_items)

# Define the checkout route
@app.route('/checkout')
def checkout():
    cart_items = CartItem.query.filter_by(user_id=session['user_id']).all()
    return render_template('checkout.html', cart_items=cart_items)

# Define the add_to_cart route
@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    toy_id = request.form.get('toy_id')
    quantity = request.form.get('quantity')
    cart_item = CartItem(toy_id=toy_id, quantity=quantity)
    db.session.add(cart_item)
    db.session.commit()
    return redirect(url_for('cart'))

# Define the remove_from_cart route
@app.route('/remove_from_cart', methods=['POST'])
def remove_from_cart():
    cart_item_id = request.form.get('cart_item_id')
    cart_item = CartItem.query.get(cart_item_id)
    db.session.delete(cart_item)
    db.session.commit()
    return redirect(url_for('cart'))

# Define the purchase route
@app.route('/purchase', methods=['POST'])
def purchase():
    cart_items = CartItem.query.filter_by(user_id=session['user_id']).all()
    for cart_item in cart_items:
        toy = Toy.query.get(cart_item.toy_id)
        toy.stock -= cart_item.quantity
        db.session.add(toy)
    db.session.commit()
    return render_template('purchase.html', cart_items=cart_items)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
