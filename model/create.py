from entry.create import create_entry

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

def generate_image(id):
  return {
    "pt-BR": {
      "sys": {
        "type": "Link",
        "linkType": "Asset",
        "id": id
      }
    }
  }

def create_brand(hero_id, image_id):
  attributes = {
    'content_type_id': 'model',
    "fields": {
      "title": {
        "pt-BR": "Model Name"
      },
      "description": {
        "pt-BR": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed et urna neque. Ut molestie velit id congue sollicitudin. Nam est metus, convallis at posuere finibus, scelerisque sed lorem. Fusce aliquet velit eget risus tristique volutpat. Vestibulum tincidunt vestibulum ornare. Praesent libero odio, volutpat sed felis at, posuere sodales ante. Ut porttitor odio massa, quis euismod mi pellentesque at. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. "
      },
      "logo": generate_image(image_id),
      "hero": generate_hero(hero_id)
    }
  }

  return create_entry(attributes)