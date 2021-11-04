from entry.create import create_entry
from logs.logging import logging
from slugify import slugify
from year.get import get_year_by_title
from year.hero.create import create_or_update_hero
from year.image.create import create_or_update_image

def create_or_update_year(entry, model):
  logging('-----')
  logging('-----')
  logging('-----')
  logging('Starting Year creation...')

  if entry is None:
    logging('Year wasn`t created. No data was passed...')
    return None
  
  year = get_year_by_title(entry['title'], model)
  hero = create_or_update_hero(entry['hero'])
  image = create_or_update_image(entry)

  if (year):
    return update_year(year, model, hero, image)

  return create_year(entry, model, hero, image)
    
def update_year(year, model, hero, image):
  logging('Updating Year...')
  # TODO: update
  return year

def create_year(entry, model, hero, image):
  attributes = {
    'content_type_id': 'year',
    "fields": {
      "title": {
        "pt-BR": entry['title']
      },
      'slug': {
        'pt-BR': slugify(entry['title'].lower())
      },
      "model": generate_entry(model['id']),
      "description": {
        "pt-BR": entry['description']
      },
      "image": generate_image(image['id']),
      "hero": generate_entry(hero['id']),
    }
  }

  return create_entry(attributes)

def generate_entry(id):
  return {
    "pt-BR": {
      "sys": {
        "type": "Link",
        "linkType": "Entry",
        "id": id
      }
    }
  }

def generate_image(id):
  return {
    "pt-BR": {
      "sys": {
        "type": "Link",
        "linkType": "Asset",
        "id": id
      }
    }
  }
