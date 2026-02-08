# Cold Email Automation: Firecrawl + Groq + SMTP

Automates cold email outreach by scraping company data from websites, generating personalized emails using AI, and sending them via SMTP—all in one workflow.

**What it does:**
1. 🕷️ Scrapes company names, descriptions, and emails from target websites
2. 🤖 Generates personalized cold emails based on the descriptions using Groq AI
3. 📧 Sends emails via SMTP (Gmail)
4. ✅ Lets you review all emails before sending

---

## Prerequisites

- Python >= 3.11
- [Firecrawl API Key](https://firecrawl.dev) (for web scraping)
- [Groq API Key](https://console.groq.com) (for AI email generation)
- Gmail account with App Password enabled

---

## Setup and Installation

### 1. Clone the repository
```bash
git clone https://github.com/Darkdev007/Cold-Email-Automation.git  
cd cold-email-automation
```

### 2. Create virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Get API Keys

**Firecrawl:**
- Sign up at https://firecrawl.dev
- Copy your API key from the dashboard

**Groq:**
- Sign up at https://console.groq.com
- Generate an API key

**Gmail App Password:**
- Enable 2-Step Verification: https://myaccount.google.com/signinoptions/two-step-verification
- Generate App Password: https://myaccount.google.com/apppasswords
- Select "Mail" → "Other" → Name it "Python Email Script"
- Copy the 16-character password

### 5. Configure environment variables

Create a `.env` file in the root directory:
```env
# API Keys
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxx
FIRECRAWL_API_KEY=fc-xxxxxxxxxxxxxxxxxxxxx

# Email Configuration
SMTP_EMAIL="your.email@gmail.com"
SMTP_PASSWORD="abcd efgh ijkl mnop" # Your 16-char app password (spaces OK)
```

---

## Usage

### Run the full automation:
```bash
python main/main.py
```

**What happens:**
1. Scrapes websites listed in `data/websites.py`
2. Generates personalized emails for each company
3. Saves all emails to `emails.json` for review
4. **Pauses** and waits for you to press ENTER
5. Sends all emails via SMTP
6. Shows success/failure for each email in terminal

### Test with a few companies first:
Edit `data/websites.py` to include only 2-3 URLs before running the full batch.

---

## Customization

### Add target companies
Edit `data/websites.py`:
```python
websites = [
    "https://company1.com/about",
    "https://company2.com/team",
    # Add more URLs here
]
```

### Customize your product pitch
Edit `src/llm.py` → Find the `PRODUCT CONTEXT` section:
```python
PRODUCT CONTEXT:
I have built [YOUR PRODUCT DESCRIPTION HERE]
```

**Current example:** Multilingual AI voice layer for Nigerian fintechs  
**Replace with:** Your actual product/service description

### Change email subject line
Edit the `generated_subject` variable in `src/llm.py`:
```python
generated_subject = "Your custom subject line here"
```

---

## Troubleshooting

**"SMTP Authentication Error"**
- Make sure you're using an App Password, not your regular Gmail password
- Double-check EMAIL_ADDRESS and SMTP_PASSWORD in `.env`

**"Firecrawl scraping failed"**
- Some websites block scrapers—try different URLs
- Check your Firecrawl API quota

**"No emails generated"**
- Check if websites.py has valid URLs
- Verify company websites have email addresses listed

---

## Important Notes

⚠️ **Review before sending:** The script pauses before sending so you can check `emails.json`  
⚠️ **Start small:** Test with 2-3 companies first  
⚠️ **Respect rate limits:** Don't send hundreds of emails at once (Gmail may flag you)  
⚠️ **Follow anti-spam laws:** Only email companies you have legitimate interest in  

---

## License
MIT

---

## Contributing
Pull requests welcome! Please open an issue first to discuss major changes.
