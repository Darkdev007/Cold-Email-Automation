import os
from groq import Groq
from dotenv import load_dotenv
import json
from src.utils import get_project_logger, return_data_path


logger = get_project_logger("LLM THINKING")
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)
emails = []
generated_subject = "Voice support for Nigerian customers"



def brain(company_data):
    for company in company_data:
        if not company["emails"]:
                continue
        prompt = f"""
        You are an expert cold email writer specializing in B2B outreach for voice AI solutions. Your task is to help me write concise, effective cold emails to fintech companies about my multilingual voice agent.

        PRODUCT CONTEXT:
        I've built a multilingual AI voice layer for Nigerian fintechs that automates customer support by resolving disputes, providing real-time transaction clarity, and managing escalations in Pidgin, Yoruba, Igbo, and Hausa—ensuring every customer is heard in their own language without needing a human agent for routine fixes.

        CORE PRINCIPLES:
        - Maximum 200 words
        - Plain language only (no AI buzzwords like "leverage," "innovative," or "cutting-edge")
        - Must include a clear, specific ask
        - Be specific, not vague (use examples, numbers, names)
        - Be honest - no fake personalization

        EMAIL STRUCTURE:
        1. WHO I AM + WHAT I DO (1-2 sentences max)
            - Brief intro that mentions the multilingual voice agent for fintech
            
        2. WHY I'M REACHING OUT (1-2 sentences)
            - Reference something SPECIFIC from their company description
            - Connect it directly to a use case for the voice agent
            
        3. WHY THEY SHOULD CARE (2-3 concrete points)
            - Focus on how the voice agent solves THEIR specific problem based on their description
            - Include tangible outcomes (time saved, cost reduced, conversion improved)
            - Use real numbers when possible
            
        4. CLEAR ASK (1 sentence question)
            - Example: "Worth a quick call next week?"

        CRITICAL CONNECTION RULE:
        For each company, I will provide their description. You MUST:
        - Identify 1-2 specific pain points or opportunities from their description
        - Explain how the multilingual voice agent directly addresses those points
        - Use their own language/terminology when relevant (if they mention "remittances," use "remittances")

        TRANSFORMATION EXAMPLES:
        ❌ "Our AI voice agent can help your fintech business"
        ✅ "Voice agent that handles customer onboarding calls in 40+ languages"

        ❌ "We provide innovative solutions"
        ✅ "Reduced support costs by 60% for payment platforms like [Example]"

        ❌ "I noticed you're doing interesting things"
        ✅ "Saw you're expanding to Latin America - our voice agent already handles Spanish, Portuguese, and 15 regional dialects"

        FORBIDDEN ELEMENTS:
        - No generic AI pitches
        - No claims about being "cutting-edge" or "revolutionary"
        - No mentioning "AI" unless necessary (focus on outcomes)
        - No vague benefits - always tie to their specific situation
        - No emails over 200 words

        INPUT FORMAT:
        - Company name : {company["name"]}
        - Company description : {company["company_mission"]}
        - Any specific notes about their market/focus

        OUTPUT REQUIRED:
        Return ONLY the email text itself. Start immediately with "Hi team {company["name"]}," or "Hey team {company["name"]},"
        Do NOT include:
        - "Here's a cold email for..."
        - "Here's the email..."
        - Any explanation or meta-commentary

        Just the email body, nothing else.
        A cold email that:
        1. Passes the "read out loud" test
        2. Shows I understand their business (using their description)
        3. Makes it crystal clear how the voice agent helps THEM specifically
        4. Feels personal, not templated """

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            max_tokens=350,
            temperature=0.3,
            messages=[{"role": "user", "content": prompt}]
        )
        emails.append({"to": company["emails"],
                "to_name": company["name"],
                "subject" : generated_subject,
                "company": company["name"],
                "body": response.choices[0].message.content
            })
        
    
    #Try and save to a file so you can go through it 
    EMAILS_PATH = return_data_path()

    with open(EMAILS_PATH, "w", encoding="utf-8") as f:
        json.dump(emails, f, indent=2, ensure_ascii=False)
        logger.info(f"Email File created at  {EMAILS_PATH}")
                  
        
