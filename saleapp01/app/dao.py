def load_categories():
    return [{
        'id': 1,
        'name': 'Mobile'
    },{
        'id': 2,
        'name': 'Tablet'
    }]
def load_products(kw=None):
    products = [{
        'id': 1,
        'name': 'Iphone X',
        'price': 100000,
        'image': "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg"
    },{
        'id': 2,
        'name': 'IPhone XS',
        'price': 100000,
        'image': "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg"
    },{
        'id': 3,
        'name': 'Iphone XIII',
        'price': 100000,
        'image': "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg"
    },{
        'id': 4,
        'name': 'Samsung 22S',
        'price': 100000,
        'image': "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg"
    },{
        'id': 5,
        'name': 'Samsung 12S',
        'price': 100000,
        'image': "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg"
    },{
        'id': 6,
        'name': 'Samsung 10S',
        'price': 100000,
        'image': "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg"
    },{
        'id': 7,
        'name': 'Samsung 11S',
        'price': 100000,
        'image': "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg"
    },{
        'id': 7,
        'name': 'Samsung 9S',
        'price': 100000,
        'image': "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg"
    }]
    if kw:
        products = [p for p in products if p['name'].lower().find(kw.lower()) >= 0]
    return products