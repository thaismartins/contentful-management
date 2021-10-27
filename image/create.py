from asset.create import create_asset
from image.get_file_details import get_file_details

def create_image(title, description, url):
  file = get_file_details(url)

  attributes = {
    "fields": {
      'title': {
        'pt-BR': title
      },
      'description': {
        'pt-BR': description
      },
      'file': {
        'pt-BR': {
          'fileName': file['name'],
          'contentType': file['content_type'],
          'upload': url
        }
      }
    }
  }

  new_asset = create_asset(attributes)
  return { 'id': new_asset.id }