from asset.create import create_asset

def create_logo():
  attributes = {
    "fields": {
      'title': {
        'pt-BR': 'Amazon Logo'
      },
      'description': {
        'pt-BR': 'Amazon Logo Description'
      },
      'file': {
        'pt-BR': {
          'fileName': 'amazon.png',
          'contentType': 'image/png',
          'upload': 'https://marcas-logos.net/wp-content/uploads/2020/01/Amazon-Logo-1.png'
        }
      }
    }
  }
  
  new_logo = create_asset(attributes)
  new_logo.process()
  new_logo.publish()
  
  return new_logo