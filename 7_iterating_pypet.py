print('Welcome to Pypet!')
print('------------------------------')

rank = {
  'star': [(0,'✰'),(1,'✰✰'),(2,'✰✰✰'),(3,'✰✰✰✰')],
  'circle': [(0,'ꔷ'),(1,'ꔷꔷ'),(2,'ꔷꔷꔷ'),(3,'ꔷꔷꔷꔷ')],
  'heart': [(0,'♥'),(1,'♥♥'),(2,'♥♥♥'),(3,'♥♥♥♥')]
}

food = {
  'va': {
    'name': 'Vitamin-A',
    'calories' : '4cal',
    'amount': '2kg'
  },
  'vb': {
    'name': 'Vitamin-B',
    'calories' : '2cal',
    'amount': '1.5kg'
  },
  'vc': {
    'name': 'Vitamin-C',
    'calories' : '1cal',
    'amount': '1kg'
  }
}

cat = {
  'name': 'Garfy',
  'type': 'cat',
  'hungry': True,
  'weight': 9.5,
  'age': 5,
  'symbol': rank['star'][2][1],
  'food': food['va'],
  'photo': '(=^o.o^=)__',
}

mouse = {
  'name': 'Fluffy',
  'type': 'mouse',
  'age': 6,
  'weight': 1.5,
  'hungry': True,
  'symbol': rank['circle'][1][1],
  'food': food['vb'],
  'photo': '<:3 )~~~~',
}

fish = {
  'name': 'Nemo',
  'type': 'fish',
  'age': 7,
  'weight': 2.1,
  'hungry': False,
  'symbol': rank['heart'][0][1],
  'food': food['vc'],
  'photo': '<`)))><',
}

pets = [cat, mouse, fish]

for pet in pets:
  print('Hello ' + pet['name'] + '!')
  print(pet['photo'])
  print('Age: ' + str(pet['age']))
  print('Rank: ' + pet['symbol'])
  print('1st Weight: ' + str(pet['weight']))
  if pet['hungry']:
    print(pet['name'] + ' is hungry!')
    calories = int(pet['food']['calories'][:1])
    amount = int(pet['food']['amount'][:1])
    pet['weight'] += calories * amount
    print('2nd Weight: ' + str(pet['weight']))
  else:
    print(pet['name'] + ' is not hungry!')

  print('------------------------------')