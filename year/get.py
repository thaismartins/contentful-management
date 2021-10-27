from logs.logging import logging
from entry.get import get_entry

def get_year_by_title(title):
  logging('Searching Year by title...')
  
  if title is None:
    return False 

  query = {
    'field': 'title',
    'value': title
  }
  
  model = get_entry(content_type_id='year', query=query)
  return model