from entry.create import create_entry

def create_brand_hero():
  attributes = {
    'content_type_id': 'sectionBrandHero',
    'fields': {
      'title': {
        'pt-BR': 'New Brand Hero'
      },
      'description':  {
        "pt-BR": {
          "nodeType": "document",
          "data": {},
          "content": [
            {
              "nodeType": "paragraph",
              "content": [
                {
                  "nodeType": "text",
                  "value": "Test Hero ",
                  "marks": [],
                  "data": {}
                },
                {
                  "nodeType": "text",
                  "value": "1234",
                  "marks": [
                    {
                      "type": "bold"
                    }
                  ],
                  "data": {}
                }
              ],
              "data": {}
            },
            {
              "nodeType": "paragraph",
              "content": [
                {
                  "nodeType": "text",
                  "value": "Test Hero ",
                  "marks": [
                    {
                      "type": "bold"
                    }
                  ],
                  "data": {}
                },
                {
                  "nodeType": "text",
                  "value": "5678",
                  "marks": [],
                  "data": {}
                }
              ],
              "data": {}
            }
          ]
        }
      }
    }
  }

  new_hero = create_entry(attributes)
  new_hero.publish()
  
  return new_hero
