# Contentful Management
This project is a POC that uses Contentful as a content manager and aims to create a bulk data upload system.

## Requirements
- Python (recommended version 3.9)

## How to start
- To run this project you need to create a account on [Contentful](https://www.contentful.com/sign-up/)
- Generate a Contentful Management Token in Settings >> API Key >> Contentful Management Token
- Export space_id, environment and token as env variable:
  
```
export CONTENTFUL_MANAGEMENT_TOKEN={your-token}
export CONTENTFUL_SPACE={your-space-id}
export CONTENTFUL_ENVIRONMENT={your-enviroment}
```

# How to run
```bash
python3 index.py
```

