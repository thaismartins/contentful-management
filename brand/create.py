from brand.get import get_brand_by_title
from brand.hero.create import create_or_update_hero
from brand.logo.create import create_or_update_logo
from entry.create import create_entry
from logs.logging import logging

def generate_hero(id):
  return {
    "pt-BR": {
      "sys": {
        "type": "Link",
        "linkType": "Entry",
        "id": id
      }
    }
  }

def generate_logo(id):
  return {
    "pt-BR": {
      "sys": {
        "type": "Link",
        "linkType": "Asset",
        "id": id
      }
    }
  }

def create_or_update_brand(entry):
  logging('-----')
  logging('-----')
  logging('-----')
  logging('Starting Brand creation...')
  
  brand = get_brand_by_title(entry['title'])

  hero = create_or_update_hero(entry['hero'])
  logo = create_or_update_logo(entry)

  if (brand):
    logging('Brand was founded!')
    return update_brand(brand, logo, hero)

  return create_brand(entry, logo, hero)

def create_brand(entry, logo, hero):
  logging('Creating Brand...')

  attributes = {
    'content_type_id': 'brand',
    "fields": {
      "title": {
        "pt-BR": entry['title']
      },
      "description": {
        'pt-BR': entry['description']
      },
      "logo": generate_logo(logo['id']),
      "hero": generate_hero(hero['id'])
    }
  }

  return create_entry(attributes)

def update_brand(brand, logo, hero):
  logging('Updating Brand...')

  # TODO: update brand
  return brand