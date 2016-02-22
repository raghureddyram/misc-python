import random

questions = {
    "strong": "Do ye like yer drinks strong?\n",
    "salty": "Do ye like it with a salty tang?\n",
    "bitter": "Are ye a lubber who likes it bitter?\n",
    "sweet": "Would ye like a bit of sweetness with yer poison?\n",
    "fruity": "Are ye one for a fruity finish?\n",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

def assess_taste():
    preferences = {}
    for flavor, question in questions.items():
        customer_response = input(question)
        if customer_response == 'y' or customer_response == 'yes':
            preferences[flavor] = True
        else:
            preferences[flavor] = False

    return preferences

def make_drink():
    preferences = assess_taste()
    drink = []
    for flavor, ingredient_choices in ingredients.items():
        if preferences[flavor]:
            drink.append(random.choice(ingredient_choices))

    print("Ingredients added to your drink are: {}.".format(", ".join(drink)))
    return drink

if __name__ == '__main__':
    make_drink()
