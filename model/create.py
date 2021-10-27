from model.image.create import create_or_update_image
from model.hero.create import create_or_update_hero
from entry.create import create_entry
from logs.logging import logging
from model.get import get_model_by_title

def create_or_update_model(entry, brand):
  logging('-----')
  logging('-----')
  logging('-----')
  logging('Starting Model creation...')

  if entry is None:
    logging('Model wasn`t created. No data was passed...')
    return None

  model = get_model_by_title(entry['title'])
  hero = create_or_update_hero(entry['hero'])
  image = create_or_update_image(entry)

  if(model):
    return update_model(model, hero, image, brand)

  return create_model(entry, hero, image, brand)

def update_model(model, hero, image, brand):
  #TODO: update model
  return model

def create_model(entry, hero, image, brand):
  attributes = {
    'content_type_id': 'model',
    "fields": {
      "title": {
        "pt-BR": entry['title']
      },
      "brand": generate_entry(brand['id']),
      "description": {
        "pt-BR": entry['description']
      },
      "image": generate_image(image['id']),
      "hero": generate_entry(hero['id']),
    }
  }

  new_model = create_entry(attributes)
  
  return { 'id': new_model.id }

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
