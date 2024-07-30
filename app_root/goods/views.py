from django.shortcuts import render


def catalog(request):
    context = {
        "title": "Home - Catalog",
        "goods": [
            {
                "image": "deps/images/goods/set of tea table and three chairs.jpg",
                "name": "Tea table and three chairs",
                "description": "A set of three chairs and a designer table for the living room.",
                "price": 30.00,
            },
            {
                "image": "deps/images/goods/set of tea table and two chairs.jpg",
                "name": "Tea table and two chairs",
                "description": "A minimalist-style set of a table and two chairs.",
                "price": 18.60,
            },
            {
                "image": "deps/images/goods/double bed.jpg",
                "name": "Double bed",
                "description": "A double bed with a headboard and very orthopedic features.",
                "price": 134.00,
            },
            {
                "image": "deps/images/goods/kitchen table.jpg",
                "name": "Kitchen table with sink",
                "description": "A kitchen table with an integrated sink and chairs for dining.",
                "price": 73.00,
            },
            {
                "image": "deps/images/goods/kitchen table 2.jpg",
                "name": "Kitchen table with built-in appliances",
                "description": "A kitchen table with a built-in stove and sink. Many shelves and overall beautiful.",
                "price": 86.00,
            },
            {
                "image": "deps/images/goods/corner sofa.jpg",
                "name": "Corner sofa for living room",
                "description": "A corner sofa that converts into a double bed, perfect for the living room and hosting guests!",
                "price": 122.00,
            },
            {
                "image": "deps/images/goods/bedside table.jpg",
                "name": "Bedside table",
                "description": "Bedside table with two drawers (flower not included).",
                "price": 11.00,
            },
            {
                "image": "deps/images/goods/sofa.jpg",
                "name": "Regular sofa",
                "description": "A regular sofa, nothing noteworthy for description.",
                "price": 38.00,
            },
            {
                "image": "deps/images/goods/office chair.jpg",
                "name": "Office chair",
                "description": "A product description about how great it is, but it's just a chair, what more can be said...",
                "price": 6.00,
            },
            {
                "image": "deps/images/goods/plants.jpg",
                "name": "Plant",
                "description": "A plant to decorate your interior, bringing freshness and tranquility.",
                "price": 2.00,
            },
            {
                "image": "deps/images/goods/flower.jpg",
                "name": "Stylized flower",
                "description": "A designer flower (possibly artificial) for interior decoration.",
                "price": 3.00,
            },
            {
                "image": "deps/images/goods/strange table.jpg",
                "name": "Bedside table",
                "description": "A table that looks quite strange but is suitable for placing next to the bed.",
                "price": 5.00,
            },
        ],
    }
    return render(request, "goods/catalog.html", context)


def product(request):
    return render(request, "goods/product.html")
