from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import Customer, Location,Product,Review,Service

from db import db
from flask_cors import CORS



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vetty.db'  # SQLite for simplicity, or your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disables track modifications (optional)
app.config['SQLALCHEMY_ECHO'] = True  # Optional: Prints SQL statements for debugging
CORS(app)
db.init_app(app)
# db = SQLAlchemy(app)

migrate = Migrate(app, db)

def create_tables():
    db.create_all()


@app.route('/', methods=['GET'])
def hello():
    return "Hello, Welcome to the Vetty API!"


# Route to get all customers
@app.route('/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()  # Get all customers from the database
    customers_data = []

    for customer in customers:
        # Manually convert the customer instance into a dictionary
        customer_data = {
            'id': customer.id,
            'name': customer.name,
            'created_at': customer.created_at,
            'image': customer.image,
            'status': customer.status,
            'is_vendor': customer.is_vendor,
            'dob': customer.dob,
            'gender': customer.gender,
            'address': {
                'street': customer.street,
                'city': customer.city,
                'state': customer.state,
                'zip': customer.zip
            },
            'contact': {
                'phone': customer.phone,
                'email': customer.email
            },
            'financial_info': {
                'bank_account_number': customer.bank_account_number,
                'bank_branch': customer.bank_branch,
                'ifsc_code': customer.ifsc_code,
                'credit_card_number': customer.credit_card_number,
                'credit_card_expiry': customer.credit_card_expiry,
                'credit_card_cvv': customer.credit_card_cvv,
                'income': customer.income
            },
            'purchase_history': {
                'order_id': customer.order_id,
                'product_id': customer.product_id,
                'purchase_date': customer.purchase_date,
                'transaction_amount': customer.transaction_amount
            },
            'preferences': {
                'product_preferences': customer.product_preferences,
                'communication_channels': customer.communication_channels,
                'feedback_given': customer.feedback_given
            },
            'interactions': {
                'customer_service_calls': customer.customer_service_calls,
                'complaints_raised': customer.complaints_raised
            },
            'social_media': {
                'facebook_profile': customer.facebook_profile,
                'twitter_profile': customer.twitter_profile,
                'posts_liked': customer.posts_liked,
                'comments_posted': customer.comments_posted
            },
            'demographic_info': {
                'age_group': customer.age_group,
                'marital_status': customer.marital_status,
                'occupation': customer.occupation
            }
        }

        customers_data.append(customer_data)

    return jsonify(customers_data)  # Return as JSON

# Route to get a specific customer by ID
@app.route('/customers/<int:id>', methods=['GET'])
def get_customer(id):
    customer = Customer.query.get(id)  # Get the customer by ID
    if customer:
        # Manually convert the customer instance into a dictionary
        customer_data = {
            'id': customer.id,
            'name': customer.name,
            'created_at': customer.created_at,
            'image': customer.image,
            'status': customer.status,
            'is_vendor': customer.is_vendor,
            'dob': customer.dob,
            'gender': customer.gender,
            'address': {
                'street': customer.street,
                'city': customer.city,
                'state': customer.state,
                'zip': customer.zip
            },
            'contact': {
                'phone': customer.phone,
                'email': customer.email
            },
            'financial_info': {
                'bank_account_number': customer.bank_account_number,
                'bank_branch': customer.bank_branch,
                'ifsc_code': customer.ifsc_code,
                'credit_card_number': customer.credit_card_number,
                'credit_card_expiry': customer.credit_card_expiry,
                'credit_card_cvv': customer.credit_card_cvv,
                'income': customer.income
            },
            'purchase_history': {
                'order_id': customer.order_id,
                'product_id': customer.product_id,
                'purchase_date': customer.purchase_date,
                'transaction_amount': customer.transaction_amount
            },
            'preferences': {
                'product_preferences': customer.product_preferences,
                'communication_channels': customer.communication_channels,
                'feedback_given': customer.feedback_given
            },
            'interactions': {
                'customer_service_calls': customer.customer_service_calls,
                'complaints_raised': customer.complaints_raised
            },
            'social_media': {
                'facebook_profile': customer.facebook_profile,
                'twitter_profile': customer.twitter_profile,
                'posts_liked': customer.posts_liked,
                'comments_posted': customer.comments_posted
            },
            'demographic_info': {
                'age_group': customer.age_group,
                'marital_status': customer.marital_status,
                'occupation': customer.occupation
            }
        }

        return jsonify(customer_data)  # Return customer data as JSON
    else:
        return jsonify({'message': 'Customer not found'}), 404  # Return 404 if customer not found


@app.route('/locations', methods=['GET'])
def get_locations():
    locations = Location.query.all()  # Get all locations from the database
    locations_data = []

    for location in locations:
        # Manually convert the location instance into a dictionary
        location_data = {
            'id': location.id,
            'name': location.name,
            'description': location.description,
            'link': location.link,
            'order': location.order,
            'status': location.status,
            'is_featured': location.is_featured,
            'image': location.image,
            'created_at': location.created_at,
            'categories': location.categories  # If categories is a pickle type, it's already in a serializable format
        }

        locations_data.append(location_data)

    return jsonify(locations_data)  # Return as JSON

# Route to get a specific location by ID
@app.route('/locations/<int:id>', methods=['GET'])
def get_location(id):
    location = Location.query.get(id)  # Get the location by ID
    if location:
        # Manually convert the location instance into a dictionary
        location_data = {
            'id': location.id,
            'name': location.name,
            'description': location.description,
            'link': location.link,
            'order': location.order,
            'status': location.status,
            'is_featured': location.is_featured,
            'image': location.image,
            'created_at': location.created_at,
            'categories': location.categories  # If categories is a pickle type, it's already in a serializable format
        }

        return jsonify(location_data)  # Return location data as JSON
    else:
        return jsonify({'message': 'Location not found'}), 404  # Return 404 if location not found



@app.route('/products', methods=['GET'])
def get_products():
    print("Fetching products...")  # Debugging line
    products = Product.query.all()
    if not products:
        print("No products found.")  # Debugging line
    products_data = []

    for product in products:
        product_data = {
            'id': product.id,
            'imageSrc': product.imageSrc,
            'title': product.title,
            'price': product.price,
            'stars': product.stars,
            'rates': product.rates,
            'discount': product.discount,
            'quantity': product.quantity,
            'type': product.type,
            'details': product.details,
            'reviews': [
                {'rating': review.rating, 'review_text': review.review_text}  # No review_id, only rating and review_text
                for review in product.reviews
            ]
        }

        products_data.append(product_data)

    return jsonify(products_data)


@app.route('/products/<int:product_id>/reviews', methods=['GET'])
def get_reviews_for_product(product_id):
    print(f"Fetching reviews for product {product_id}...")  # Debugging line

    # Query reviews based on the product_id
    product_reviews = Review.query.filter_by(product_id=product_id).all()

    # If no reviews are found for this product
    if not product_reviews:
        return jsonify({"message": "No reviews found for this product."}), 404

    # Constructing the response data
    reviews_data = [
        {
            'review_id': review.review_id,
            'customer_id': review.customer_id,
            'rating': review.rating,
            'review_text': review.review_text,
            'review_date': review.review_date.strftime('%Y-%m-%d'),  # Format the date as string
            'status': review.status
        }
        for review in product_reviews
    ]

    return jsonify(reviews_data)


@app.route('/reviews', methods=['GET'])
def get_all_reviews():
    print("Fetching all reviews...")  # Debugging line

    # Query all reviews from the database
    reviews = Review.query.all()

    # If no reviews are found
    if not reviews:
        return jsonify({"message": "No reviews found."}), 404

    # Constructing the response data
    reviews_data = [
        {
            'review_id': review.review_id,
            'product_id': review.product_id,
            'customer_id': review.customer_id,
            'rating': review.rating,
            'review_text': review.review_text,
            'review_date': review.review_date.strftime('%Y-%m-%d'),  # Format the date as string
            'status': review.status
        }
        for review in reviews
    ]

    return jsonify(reviews_data)

@app.route('/services', methods=['GET'])
def get_all_services():
    print("Fetching all services...")  # Debugging line

    # Query all services from the database
    services = Service.query.all()

    # If no services are found
    if not services:
        return jsonify({"message": "No services found."}), 404

    # Constructing the response data
    services_data = [
        {
            'id': service.id,
            'service_type': service.service_type,
            'name': service.name,
            'description': service.description,
            'price': service.price,
            'image_url': service.image_url
        }
        for service in services
    ]

    return jsonify(services_data), 200



# if __name__ == "__main__":
#     app.run(port=5000, host='0.0.0.0', debug=False)

if __name__ == "__main__":
    # Get the port from the environment variable or default to 5000
    import os
    port = int(os.environ.get("PORT", 5000))

    # Make sure the app is listening on all interfaces (0.0.0.0) for cloud deployments
    app.run(host='0.0.0.0', port=port, debug=False)