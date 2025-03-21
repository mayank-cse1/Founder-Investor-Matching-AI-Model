import os
import json
import time
from google import genai
from google.genai import types
from dotenv import load_dotenv
from models import WEIGHTS, MatchScore

# Load environment variables
load_dotenv()

# Initialize Gemini API Client
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

def get_summary(founder_data, investor_score):
    """Generates a summary response for founders using Gemini AI."""
    prompt = f"""
    You're an investment management firm that specializes in connecting founders with potential investors. 
    Given the following profiles and match scores, generate a professional yet engaging conversation response for the founder seeking investment.

    Founder question:
    {founder_data}

    Investor Match:
    {investor_score}

    Your response should sound like a knowledgeable advisor, highlighting the strengths of the match and encouraging the founder to explore this investment opportunity.

    It should be a conversational response to the founder's question, well-structured and professionally formatted.
    """
    
    response = client.models.generate_content(
        model='gemini-2.0-flash',
        contents=prompt
    )
    return response.text.strip().replace("\n", "\n\n")

def get_match_score(investor_id, investor_data, founder_id, founder_data):
    """Calls Gemini API to get a match score between investors and founders."""
    prompt = f"""
    Given the following Founder and Investor profiles, rate their compatibility on a scale of 1 to 10:
    
    Founder Profile:
    {founder_data}
    
    Investor Profile:
    {investor_data}
    
    Justify the score based on industry match, funding fit, and startup stage alignment.

    Note: If any information is missing, rate the criteria as zero.
    """

    response = client.models.generate_content(
        model='gemini-2.0-flash',
        contents=prompt,
        config={
            'response_mime_type': 'application/json',
            'response_schema': MatchScore,
        },
    )
    
    return json.loads(response.text.strip())

def compute_final_score(criteria):
    """Computes the final weighted match score based on individual criteria."""
    MAX_POSSIBLE_SCORE = sum(weight * 10 for weight in WEIGHTS.values())  # Normalize to 100

    total_score = sum(
        criteria[key][key] * weight
        for key, weight in WEIGHTS.items()
        if key in criteria
    )
    return round((total_score / MAX_POSSIBLE_SCORE) * 100)