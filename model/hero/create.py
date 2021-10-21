from entry.create import create_entry
from rich_text.create import create_rich_text

def create_model_hero():
  attributes = {
    'content_type_id': 'sectionModelHero',
    'fields': {
      'title': {
        'pt-BR': 'New Model Hero'
      },
      'description':  {
        "pt-BR": create_rich_text()
      }
    }
  }

  new_hero = create_entry(attributes)
  new_hero.publish()
  
  return new_hero
