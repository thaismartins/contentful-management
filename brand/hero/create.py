from entry.create import create_entry
from entry.get import get_entry
from image.create import create_image
from image.get import get_image
from rich_text.convert_html import convert_html
from logs.logging import logging

def create_or_update_hero(entry):
  logging('-----')
  logging('Starting Brand | Hero creation...')

  if entry is None:
    logging('Brand | Hero wasn`t created. No data was passed...')
    return None
    
  image = create_or_update_image(entry)
  hero = get_hero(entry)
  if (hero):
    return update_hero(hero, image)

  return create_hero(entry, image)
  
def update_hero(entry, image):
  logging('Updating Brand | Hero...')
  # TODO: update hero
  return entry

def create_hero(entry, image):
  logging('Creating Brand | Hero...')

  description = convert_html(entry['description'])
  attributes = {
    'content_type_id': 'sectionBrandHero',
    'fields': {
      'title': {
        'pt-BR': entry['title']
      },
      'description':  {
        "pt-BR": description
      },
      'image': {
        'pt-BR': generate_image(image)
      }
    }
  }

  new_hero = create_entry(attributes)
  # new_hero.publish()
  
  return { 'id': new_hero.id }

def get_hero(entry):
  query = { 
    'field': 'title',
    'value': entry['title']
  }
  return get_entry(content_type_id='sectionBrandHero', query=query)

def create_or_update_image(entry):
  if entry is None or 'image' not in entry:
    logging('Brand | Hero - Image wasn`t created. No data was passed...')
    return None

  image = get_image(entry['image'])
  if (image):
    logging('Returning Brand | Hero - Image...')
    return image

  logging('Creating Brand | Hero - Image..')

  title = entry['title']
  description = f"{entry['title']} Description"

  return create_image(title, description, entry['image'])

def generate_image(image):
  return {
    "sys": {
      "type": "Link",
      "linkType": "Asset",
      "id": image['id']
    }
  }