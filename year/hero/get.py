from logs.logging import logging
from entry.get import get_entry

def get_hero_by_title(title):
  logging('Searching Year | Hero by title...')
  
  if title is None:
    return None 

  query = {
    'field': 'title',
    'value': title
  }
  
  model = get_entry(content_type_id='sectionYearHero', query=query)
  return model