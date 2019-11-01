from random import randint, sample, uniform
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']


def generate_products(num_products=30):
    """generates a list of products"""
    products = []
    for _ in range(num_products):
        name = sample(ADJECTIVES, 1)[0] + ' ' + sample(NOUNS, 1)[0]
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(0.0, 2.5)
        prod = Product(name=name, price=price,
                       weight=weight, flammability=flammability)
        products.append(prod)

    return products


def inventory_report(products):
    """Loop over the products to calculate the report."""
    names = []
    prices = []
    weights = []
    flammabilities = []

    for product in generate_products():
        names.append(product.name)
        prices.append(product.price)
        weights.append(product.weight)
        flammabilities.append(product.flammability)

    unique_names = len(products)
    avg_price = sum(prices) / len(prices)
    avg_weight = sum(weights) / len(weights)
    avg_flammability = sum(flammabilities) / len(flammabilities)

    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print('Unique product names: ', unique_names)
    print('Average price: ', avg_price)
    print('Average weight: ', avg_weight)
    print('Average flammability: ', avg_flammability)


if __name__ == '__main__':
    inventory_report(generate_products())
