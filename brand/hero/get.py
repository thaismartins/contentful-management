from entry.get import get_entry
from logs.logging import logging

def get_hero_by_title(title):
  logging('Searching Brand | Hero by title...')
  
  if title is None:
    return False 

  query = {
    'field': 'title',
    'value': title
  }
  
  hero = get_entry(content_type_id='sectionBrandHero', query=query)
  return hero