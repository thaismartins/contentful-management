from asset.create import create_asset
from brand.logo.get import get_logo

def create_or_update_logo(entry):
  if entry is None:
    print('Brand - Logo wasn`t created. No data was passed...')

  logo = get_logo(entry)
  if(logo):
    return update_logo(logo)

  return create_logo()
  
def create_logo():
  print('Creating Brand - Logo...')

  attributes = {
    "fields": {
      'title': {
        'pt-BR': 'Brand Logo'
      },
      'description': {
        'pt-BR': 'Brand Logo Description'
      },
      'file': {
        'pt-BR': {
          'fileName': 'logo.jpg',
          'contentType': 'image/jpg',
          'upload': 'https://www.fiat.com.br/content/dam/fiat/open_graph_rebrand/Home_Fiat.jpg'
        }
      }
    }
  }
  
  return create_asset(attributes)

def update_logo(logo):
  print('Updating Brand - Logo...')

  # TODO: update logo
  # if (file_name != ''):
  # logo.delete()
  # logo = create_logo()

  # file_name = logo['file']['pt-BR']['fileName']
  return logo