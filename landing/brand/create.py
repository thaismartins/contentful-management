from brand.hero.create import create_brand_hero
from brand.create import create_brand
from brand.logo.create import create_logo

def create_landing_brand():
  new_hero = create_brand_hero()
  print(new_hero.id)

  new_logo = create_logo()
  print(new_logo.id)

  new_brand = create_brand(new_hero.id, new_logo.id)
  print(new_brand.id)

  return new_brand.id