import json
from entry.create import create_entry
from logs.logging import logging
from model.hero.get import get_hero_by_title
from model.hero.image.create import create_or_update_images
from rich_text.convert_html import convert_html

def create_or_update_hero(entry):
  logging('-----')
  logging('Starting Model | Hero creation...')

  if entry is None:
    logging('Model | Hero wasn`t created. No data was passed...')
    return None

  images = create_or_update_images(entry)
  hero = get_hero_by_title(entry['title'])

  if(hero):
    return update_hero(hero, images)

  return create_hero(entry, images)

def update_hero(hero, images):
  # TODO: update hero
  return hero

def create_hero(entry, images):
  imagesEntry = []
  if images is not None:
    for image in images:
      imagesEntry.append(generate_image(image['id']))

  description = convert_html(entry['description'])

  attributes = {
    'content_type_id': 'sectionModelHero',
    'fields': {
      'title': {
        'pt-BR': entry['title']
      },
      'description':  {
        "pt-BR": description
      },
      'images': {
        'pt-BR': imagesEntry
      }
    }
  }

  new_hero = create_entry(attributes)
  # new_hero.publish()

  return { 'id': new_hero.id }

def generate_image(id): 
  return {
    "sys": {
      "type": "Link",
      "linkType": "Asset",
      "id": id
    }
  }
