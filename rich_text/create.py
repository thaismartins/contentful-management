def create_rich_text():
  return {
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
            "marks": [
              {
                "type": "italic"
              }
            ],
            "data": {}
          }
        ],
        "data": {}
      }
    ]
  }