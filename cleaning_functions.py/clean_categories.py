def clean_categories(x):
    if (x in ['Milk and milk products excluding cheese']):
        return "Milk products exc. cheese"
    elif (x in ['Cheese']):
        return "Cheese"
    elif (x in ['Carcase meat','Non-carcase meat and meat products']):
        return "Meat"
    elif (x in ['Fish']):
        return "Fish"
    elif (x in ['Eggs']):
        return "Eggs"
    elif (x in ['Fats']):
        return "Fats"
    elif (x in ['Sugar and preserves']):
        return "Sugar and preserves"
    elif (x in ['Fresh and processed potatoes','Processed potatoes']):
        return "Potatoes"
    elif (x in ['Fresh and processed vegetables, excluding potatoes']):
        return "Vegetables exc. Potatoes"
    elif (x in ['Fresh fruit','Processed fruit and fruit products']):
        return "Fruit"
    elif (x in ['White bread','Brown and wholemeal bread']):
        return "Bread"
    elif (x in ['Flour']):
        return "Flour"
    elif (x in ['Cakes, buns and pastries']):
        return "Cakes, buns and pastries"
    elif (x in ['Biscuits and crispbreads']):
        return "Biscuits"
    elif (x in ['Other cereals and cereal products']):
        return "Other cereals and cereal products"
    elif (x in ['Beverages']):
        return "Tea and Coffee"
    elif (x in ['Other food and drink']):
        return "Other food and drink"
    elif (x in ['Soft drinks']):
        return "Soft drinks"
    elif (x in ['Confectionery']):
        return "Confectionery"
    elif (x in ['Alcoholic drinks']):
        return "Alcoholic drinks"
    else: return "Minor food group"