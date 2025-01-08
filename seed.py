from app import app, db
from models import Customer,Location,Product,Review,Service
from datetime import datetime
import sqlite3



def create_customer_data():
    # Sample customers (you can add more)
    customers = [
        Customer(
            name="Jaime Lannister",
            created_at="2022-05-10",
            image="https://placehold.co/300/f5f5f5/b0b0b0ff.webp",
            status="Active",
            is_vendor=False,
            dob="1985-03-15",
            gender="Female",
            street="123 Elm St",
            city="Anytown",
            state="CA",
            zip="12345",
            phone="555-1234",
            email="jaime@gmail.com",
            bank_account_number="9876543210",
            bank_branch="Downtown Branch",
            ifsc_code="ABCD1234",
            credit_card_number="**** **** **** 5678",
            credit_card_expiry="09/23",
            credit_card_cvv="***",
            income="$80000",
            order_id=101,
            product_id=1,
            purchase_date="2022-06-20",
            transaction_amount="$500",
            product_preferences="Electronics, Home Decor",
            communication_channels="Email, Phone",
            feedback_given=True,
            customer_service_calls=2,
            complaints_raised=1,
            facebook_profile="jaime.lannister",
            twitter_profile="jaime_l",
            posts_liked=20,
            comments_posted=5,
            age_group="30-40",
            marital_status="Married",
            occupation="Knight"
        ),
        Customer(
            name="Daenerys Targaryen",
            created_at="2022-04-18",
            image="https://placehold.co/300/f5f5f5/b0b0b0ff.webp",
            status="Active",
            is_vendor=False,
            dob="1978-12-10",
            gender="Male",
            street="456 Dragonstone",
            city="King's Landing",
            state="Westeros",
            zip="67890",
            phone="555-5678",
            email="daenerys@gmail.com",
            bank_account_number="1234567890",
            bank_branch="Iron Bank",
            ifsc_code="EFGH5678",
            credit_card_number="**** **** **** 1234",
            credit_card_expiry="11/24",
            credit_card_cvv="****",
            income="$100000",
            order_id=102,
            product_id=2,
            purchase_date="2022-07-15",
            transaction_amount="$1200",
            product_preferences="Dragons, Fire",
            communication_channels="Phone, Social Media",
            feedback_given=True,
            customer_service_calls=1,
            complaints_raised=0,
            facebook_profile="daenerys.targaryen",
            twitter_profile="daenerys_q",
            posts_liked=50,
            comments_posted=10,
            age_group="40-50",
            marital_status="Single",
            occupation="Queen"
        ),

    ]

    # Insert customers
    for customer in customers:
        db.session.add(customer)

    # Commit all data
    db.session.commit()


def create_location_data():
    # Sample locations
    locations = [
        Location(
            name="QuickMart",
            description="Athletic footwear and apparel company",
            link="https://nike.com",
            order=1,
            status="Active",
            is_featured=True,
            image="https://placehold.co/1000/f5f5f5/b0b0b0ff.webp",
            categories=[1, 2, 3],  # Category IDs as list
            created_at="2023-10-09"
        ),
        Location(
            name="Magunas",
            description="Multinational beverage corporation",
            link="https://coca-cola.com",
            order=2,
            status="Active",
            is_featured=False,
            image="https://placehold.co/1000/f5f5f5/b0b0b0ff.webp",
            categories=[4, 5, 6],
            created_at="2023-10-09"
        ),
        Location(
            name="EastMart",
            description="Location of adhesive bandages",
            link="https://band-aid.com",
            order=3,
            status="Active",
            is_featured=True,
            image="https://placehold.co/1000/f5f5f5/b0b0b0ff.webp",
            categories=[7, 8],
            created_at="2023-10-09"
        ),
        Location(
            name="Khetias",
            description="Multinational corporation that designs and manufactures sports shoes, clothing, and accessories",
            link="https://adidas.com",
            order=4,
            status="Active",
            is_featured=False,
            image="https://placehold.co/1000/f5f5f5/b0b0b0ff.webp",
            categories=[9, 10],
            created_at="2023-10-09"
        ),
        Location(
            name="Cleanshelf",
            description="Multinational technology company that designs, manufactures, and sells consumer electronics, computer software, and online services",
            link="https://apple.com",
            order=5,
            status="Active",
            is_featured=True,
            image="https://placehold.co/1000/f5f5f5/b0b0b0ff.webp",
            categories=[11, 12],
            created_at="2023-10-09"
        ),
        Location(
            name="KSPCA",
            description="Multinational technology company focusing on e-commerce, cloud computing, and artificial intelligence",
            link="https://amazon.com",
            order=6,
            status="Active",
            is_featured=False,
            image="https://placehold.co/1000/f5f5f5/b0b0b0ff.webp",
            categories=[13, 14],
            created_at="2023-10-09"
        ),
        Location(
            name="Carrefour",
            description="Multinational food and beverage company",
            link="https://nestle.com",
            order=7,
            status="Active",
            is_featured=True,
            image="https://placehold.co/1000/f5f5f5/b0b0b0ff.webp",
            categories=[15, 16],
            created_at="2023-10-09"
        ),
        Location(
            name="Sayen",
            description="Multinational technology company that specializes in Internet-related services and products",
            link="https://google.com",
            order=8,
            status="Active",
            is_featured=False,
            image="https://placehold.co/1000/f5f5f5/b0b0b0ff.webp",
            categories=[17, 18],
            created_at="2023-10-09"
        ),
        Location(
            name="FoodPlus",
            description="Multinational technology company focusing on e-commerce, cloud computing, and artificial intelligence",
            link="https://amazon.com",
            order=9,
            status="Active",
            is_featured=True,
            image="https://placehold.co/1000/f5f5f5/b0b0b0ff.webp",
            categories=[19, 20],
            created_at="2023-10-09"
        ),
        Location(
            name="Gilanis",
            description="Multinational food and beverage company",
            link="https://nestle.com",
            order=10,
            status="Active",
            is_featured=False,
            image="https://placehold.co/1000/f5f5f5/b0b0b0ff.webp",
            categories=[21, 22],
            created_at="2023-10-09"
        )
    ]

    # Insert the data into the database
    for location in locations:
        db.session.add(location)  # Add each location to the session

    # Commit the session to save the locations to the database
    db.session.commit()

    print("Location data inserted successfully.")



def create_product_data():
    # Sample product data
    products = [
        Product(
            id=0,
            imageSrc="https://ke.jumia.is/unsafe/fit-in/680x680/filters:fill(white)/product/47/8330882/1.jpg?2246",
            title="Krunshi Plus",
            price=960.0,  # Price should be float
            stars=4,
            rates=53,
            discount="0",  # Assuming discount is in percentage format as a string, or an empty string if no discount
            quantity=0,
            type="Pet Food",
            details="Details"
        ),
        Product(
            id=1,
            imageSrc="https://i.pinimg.com/736x/d1/6b/8a/d16b8a63cfdf592966af5db420ab16f4.jpg",
            title="Pet Collar",
            price=360.0,
            stars=5,
            rates=87,
            discount="0",
            quantity=0,
            type="Pet Accessories",
            details="Details about the collar"
        ),
        Product(
            id=2,
            imageSrc="https://ke.jumia.is/unsafe/fit-in/680x680/filters:fill(white)/product/89/0430882/1.jpg?2333",
            title="Dog Rice",
            price=100.0,
            stars=3,
            rates=24,
            discount="0",
            quantity=0,
            type="Pet Food",
            details="Details about the dog food"
        ),
        Product(
            id=3,
            imageSrc="https://i.pinimg.com/736x/71/53/aa/7153aa3a28efc418cb75e4202eea1cfe.jpg",
            title="Pumpkin brush",
            price=700.0,
            stars=4,
            rates=65,
            discount="0",
            quantity=0,
            type="Pet Accessories",
            details="Details"
        ),
        Product(
            id=4,
            imageSrc="https://media.istockphoto.com/id/1801414577/photo/close-up-a-man-applying-tick-and-flea-prevention-treatment-and-medicine-to-her-dog-or-pet.webp?a=1&b=1&s=612x612&w=0&k=20&c=ZnZMdkw9GySUAt9zfw_flxAMkeCvopW630D0dXGGgLY=",
            title="Pet Medication",
            price=500.0,
            stars=3,
            rates=40,
            discount="0",
            quantity=0,
            type="Pet Health",
            details="Details"
        ),
        Product(
            id=5,
            imageSrc="https://i.pinimg.com/736x/d9/98/d4/d998d4a1b942a451c52af088b101803e.jpg",
            title="Human Dog bed",
            price=660.0,
            stars=4,
            rates=92,
            discount="40",  # Assuming discount is a percentage value
            quantity=0,
            type="Accessories",
            details="Support for Comfort: It features soothing and warm faux shag fur supported with 3.2 memory foam. This combination distributes weight evenly, providing optimal pressure relief and joint support for you and your pet."
        ),
        Product(
            id=6,
            imageSrc="https://i.pinimg.com/736x/2e/af/0d/2eaf0d16b87ba616fac128dbbbddc0c3.jpg",
            title="Pet Brush",
            price=660.0,
            stars=5,
            rates=77,
            discount="40",  # Assuming discount is a percentage value
            quantity=0,
            type="Pet Accessories",
            details="Details"
        ),
        Product(
            id=7,
            imageSrc="https://i.pinimg.com/736x/6c/0e/72/6c0e725c790125d72629176caa440e2d.jpg",
            title="Royal Canin",
            price=360.0,
            stars=4,
            rates=59,
            discount="40",  # Assuming discount is a percentage value
            quantity=0,
            type="Pet Accessories",
            details="Details"
        ),
        Product(
            id=8,
            imageSrc="https://ke.jumia.is/unsafe/fit-in/680x680/filters:fill(white)/product/90/3384882/1.jpg?4500",
            title="Krunshi Economy",
            price=160.0,
            stars=3,
            rates=70,
            discount="40",  # Assuming discount is a percentage value
            quantity=0,
            type="Pet Food",
            details="Details"
        ),
        Product(
            id=9,
            imageSrc="https://ke.jumia.is/unsafe/fit-in/680x680/filters:fill(white)/product/96/5574511/1.jpg?0616",
            title="Bravo",
            price=1160.0,
            stars=5,
            rates=33,
            discount="40",  # Assuming discount is a percentage value
            quantity=0,
            type="Pet Food",
            details="Details"
        ),
        Product(
            id=10,
            imageSrc="https://ke.jumia.is/unsafe/fit-in/680x680/filters:fill(white)/product/98/8530682/1.jpg?0755",
            title="Food Bowl",
            price=360.0,
            stars=4,
            rates=95,
            discount="40",  # Assuming discount is a percentage value
            quantity=0,
            type="Pet Accessories",
            details="Details"
        )
        # Add more products here as needed...
    ]

    # Insert products into the database
    for product in products:
        db.session.add(product)

    # Commit changes to the database
    db.session.commit()




def create_review_data():
    # Sample review data
    reviews = [
        Review(
            product_id=3,
            customer_id=1,
            rating=5,
            review_text="This product is amazing! It exceeded my expectations and I highly recommend it.",
            review_date=datetime(2022, 8, 15),  # Correct use of datetime
            status="Approved"
        ),
        Review(
            product_id=10,
            customer_id=2,
            rating=4,
            review_text="Good quality product. It serves its purpose well.",
            review_date=datetime(2022, 8, 16),
            status="Pending"
        ),
        Review(
            product_id=4,
            customer_id=3,
            rating=3,
            review_text="The product is okay, but I expected better quality for the price.",
            review_date=datetime(2022, 8, 17),
            status="Rejected"
        ),
        Review(
            product_id=1,
            customer_id=4,
            rating=2,
            review_text="Not satisfied with the product. It broke after just a few uses.",
            review_date=datetime(2022, 8, 18),
            status="Approved"
        ),
        Review(
            product_id=8,
            customer_id=5,
            rating=1,
            review_text="Terrible product! It didn't work at all. I want a refund.",
            review_date=datetime(2022, 8, 19),
            status="Pending"
        ),
    ]

    # Insert reviews into the database
    for review in reviews:
        db.session.add(review)

    # Commit changes to the database
    db.session.commit()

    print("Sample review data inserted successfully.")

def create_service_data():
    # Sample service data
    services = [
        Service(
            service_type="Pet Grooming",
            name="Full Body Grooming",
            description="A full-body grooming service for cats and dogs, including wash, trim, and nail clipping.",
            price=50,
            image_url="https://media.istockphoto.com/id/1393558296/photo/dog-taking-bath-at-home-n.webp?a=1&b=1&s=612x612&w=0&k=20&c=aRaRfyIeVdYKlPJ13ojDTyUQEUjkDpOCZtotIc56Lh0="
        ),
        Service(
            service_type="Vaccination",
            name="Dog Vaccination",
            description="Complete vaccination for dogs, including rabies, parvo, and distemper.",
            price=100,
            image_url="https://media.istockphoto.com/id/513595916/photo/vets-giving-shot-to-a-puppy.webp?a=1&b=1&s=612x612&w=0&k=20&c=SiSbnqwbxH3-qVFehXDYhQD-FtNOlun93as0FDkRDU0="
        ),
        Service(
            service_type="Vaccination",
            name="Cat Vaccination",
            description="Comprehensive vaccination for cats, covering feline leukemia, rabies, and more.",
            price=90,
            image_url="https://media.istockphoto.com/id/1352655350/photo/female-veterinarian-doctor-is-giving-an-injection-to-a-cat.webp?a=1&b=1&s=612x612&w=0&k=20&c=wJ-fFEWbiJEEsUuaDvYXGZRed0Ytm0Ui16rtnhcPm0Y="
        ),
        Service(
            service_type="Consultation",
            name="Veterinary Consultation",
            description="One-on-one consultation with a certified vet to diagnose and discuss your pet's health.",
            price=60,
            image_url="https://media.istockphoto.com/id/638142534/photo/examining-a-kitten.webp?a=1&b=1&s=612x612&w=0&k=20&c=91rpW-PRqAcPXBkuGkWETzDARFsk0SWZ07U_NkU9ugI="
        ),
        Service(
            service_type="Pet Food",
            name="Fish Pellets",
            description="High-quality fish pellets for aquatic pets like goldfish and bettas.",
            price=15,
            image_url="https://media.istockphoto.com/id/1091670812/photo/close-up-on-animal-food.webp?a=1&b=1&s=612x612&w=0&k=20&c=p0rOVxn5SMRRTEs3gyvCPt9KlcUCiaUTPbV3YuNRDcE="
        ),
        Service(
            service_type="Pet Food",
            name="Chicken Pet Food",
            description="Premium chicken-based pet food for both cats and dogs.",
            price=25,
            image_url="https://media.istockphoto.com/id/2182380119/photo/chickens-eating-from-a-feeder-at-a-poultry-farm.webp?a=1&b=1&s=612x612&w=0&k=20&c=I9Cp9-SQ_Z1m6AJPnVIc8F72uJu2lr5yASZBV314o2Y="
        ),
        Service(
            service_type="Pet Accessories",
            name="Pet Collar",
            description="A durable, adjustable collar for your pet, available in various sizes.",
            price=20,
            image_url="https://media.istockphoto.com/id/1248454290/photo/accessories-for-cat-and-dog-on-blue-background-pet-mathanie-and-eastmarting-concept-flat-lay-top-view.webp?a=1&b=1&s=612x612&w=0&k=20&c=OXwUAjrAZHgrIb5YxOpv-XhqTN82bwHoQJBzsNDCkuk="
        ),
        Service(
            service_type="Pet Medication",
            name="Flea Treatment",
            description="Effective flea treatment for dogs and cats.",
            price=40,
            image_url="https://media.istockphoto.com/id/1801414577/photo/close-up-a-man-applying-tick-and-flea-prevention-treatment-and-medicine-to-her-dog-or-pet.webp?a=1&b=1&s=612x612&w=0&k=20&c=ZnZMdkw9GySUAt9zfw_flxAMkeCvopW630D0dXGGgLY="
        ),
        Service(
            service_type="Pet Health",
            name="Pet Multivitamins",
            description="Multivitamins for overall health and wellness of pets.",
            price=30,
            image_url="https://media.istockphoto.com/id/184941787/photo/senior-golden-retriever-taking-daily-medication.webp?a=1&b=1&s=612x612&w=0&k=20&c=qrawYq9yELKnlHC113yjaP2O9mHZfK8KodZKaV6teGA="
        )
    ]

    # Insert services into the database
    for service in services:
        db.session.add(service)

    # Commit changes to the database
    db.session.commit()

    print("Sample service data inserted successfully.")

if __name__ == '__main__':
    with app.app_context():
        # Create all tables
        db.create_all()

        # Populate database
        create_customer_data()
        create_location_data()
        create_product_data()
        create_review_data()
        create_service_data()


        print("Database seeded successfully!")