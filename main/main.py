from src.utils import get_project_logger
from src.data_scraping import scrape_data
from src.llm import brain
from src.email_utils import send_emails

logger = get_project_logger("main")

def main():
    # Scrape description, name and email from given data
    company_data = scrape_data()
    

    # Generate Cold email pitch based on the description of the company
    brain(company_data)

    # Wait for user to review and proceed
    input("Review the emails.json file press ENTER once done")

    send_emails()


if __name__ == "__main__":
    main()