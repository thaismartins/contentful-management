from logs.logging import logging
from entry.create import create_entry
from rich_text.convert_html import convert_html
from brand.hero.image.create import create_or_update_image
from brand.hero.get import get_hero_by_title

def create_or_update_hero(entry):
  logging('-----')
  logging('Starting Brand | Hero creation...')

  if entry is None:
    logging('Brand | Hero wasn`t created. No data was passed...')
    return None
    
  image = create_or_update_image(entry)
  hero = get_hero_by_title(entry['title'])
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

def generate_image(image):
  return {
    "sys": {
      "type": "Link",
      "linkType": "Asset",
      "id": image['id']
    }
  }