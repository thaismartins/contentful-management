from image.get import get_image
from logs.logging import logging

def get_logo(entry):
  if entry is None or 'logo' not in entry:
    logging('Brand | Logo wasn`t created. No data was passed...')
    return None

  logging('Returning Brand | Logo...')
  return get_image(entry['logo'])