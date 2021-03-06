import csv

# import logging
# logging.basicConfig(level=logging.DEBUG)

from brand.create import create_or_update_brand
from model.create import create_or_update_model
from year.create import create_or_update_year

def create_contents():
  with open('/Users/thaismartins/Desktop/carros.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
      brand = generate_brand(row)
      new_brand = create_or_update_brand(brand)

      model = generate_model(row)
      new_model = create_or_update_model(model, new_brand)

      year = generate_year(row)
      new_year = create_or_update_year(year, new_model)

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
    'image': data['model_image'],
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
    'image': data['year_image'],
    'hero': {
      'title': data['year_hero_title'],
      'description': data['year_hero_description'],
      'images': data['year_hero_images'].split(sep=' | '),
    }
  }

create_contents()
