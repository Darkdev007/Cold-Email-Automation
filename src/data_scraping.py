from firecrawl.v2.utils.error_handler import InternalServerError
from pydantic import BaseModel
from firecrawl import Firecrawl
from dotenv import load_dotenv
from typing import List
from data.websites import nigeria_startup_websites
import os
from src.utils import get_project_logger

load_dotenv()

logger = get_project_logger("data_scrapping")

api_key = os.getenv("FIRECRAWL_API_KEY")
firecrawl = Firecrawl(api_key=api_key)
company_data = []

class CompanyInfo(BaseModel):
  name : str
  company_mission : str
  emails: List[str]

def scrape_data():
    for startup in nigeria_startup_websites:
        url = startup
        try:
            result = firecrawl.scrape(
                url,
                formats=[{
                "type": "json",
                "schema": CompanyInfo.model_json_schema()
                }],
                only_main_content=True,
                timeout=120000
            )
            company_data.append(result.json)
            logger.info(f"Scraped {url} successfully")
        except InternalServerError as e:
            logger.info(f"Failed completely for {url}: {e}")
            company_data.append({"company_mission": "","emails": []})

    return company_data


    
