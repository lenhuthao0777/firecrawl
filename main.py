from firecrawl import FirecrawlApp
from pydantic import BaseModel, Field
import os
from dotenv import load_dotenv

api_key = os.getenv('API_KEY')

load_dotenv()

# Initialize the FirecrawlApp with your API key
app = FirecrawlApp(api_key=api_key)

class ExtractSchema(BaseModel):
    company_mission: str
    supports_sso: bool
    is_open_source: bool
    is_in_yc: bool

data = app.scrape_url('https://docs.firecrawl.dev/', {
    'formats': ['json'],
    'jsonOptions': {
        'schema': ExtractSchema.model_json_schema(),
    }
})
print(data["json"])