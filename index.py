import csv

# import logging
# logging.basicConfig(level=logging.DEBUG)

from brand.create import create_or_update_brand

def create_contents():
  with open('/Users/thaismartins/Desktop/carros.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:

      brand = generate_brand(row)
      new_brand = create_or_update_brand(brand)

      # model = generate_model(row)
      # year = generate_year(row)

def generate_brand(data):
  return {
    'title': data['brand'],
    'description': data['brand_description'],
    'logo': data['brand_logo'],
    'hero': {
      'title': data['brand_hero_title'],
      'description': data['brand_hero_description'],
      'image': data['brand_hero_image'],
    }
  }

def generate_model(data):
  return {
    'title': data['model'],
    'description': data['model_description'],
    'hero': {
      'title': data['model_hero_title'],
      'description': data['model_hero_description'],
      'images': data['model_hero_images'].split(sep=' | '),
    }
  }

def generate_year(data):
  return {
    'title': data['year'],
    'description': data['year_description'],
    'hero': {
      'title': data['model_hero_title'],
      'description': data['model_hero_description'],
      'images': data['model_hero_images'].split(sep=' | '),
    }
  }

create_contents()
