from logs.logging import logging
from image.create import create_image
from image.get import get_image

def create_or_update_images(entry):
  logging('Creating Model | Hero - Images...')

  if entry['images'] is None:
    return None
  
  images = []
  for image in entry['images']:
    imageEntry = dict(entry)
    imageEntry['image'] = image
    images.append(create_or_update_image(imageEntry))

  return images

def create_or_update_image(entry):
  logging('Creating Model | Hero - Image...')

  if entry is None or 'image' not in entry:
    logging('Model | Hero - Image wasn`t created. No data was passed...')
    return None

  image = get_image(entry['image'])
  if (image):
    logging('Returning Model | Hero - Image...')
    return image

  logging('Creating Model | Hero - Image..')

  title = entry['title']
  description = f"{entry['title']} Description"

  new_image = create_image(title, description, entry['image'])

  return { 'id': new_image.id }
