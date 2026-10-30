import os
from google import genai

# 1. SCM Email Optimization Engine
def generate_vendor_email_via_ai(context_data, tone="professional"):
    """Uses Google Gemini API to auto-draft critical supply chain communications using the new Interactions API."""
    # This is safe for GitHub as no API key is hardcoded; it automatically loads from the environment.
    client = genai.Client()
    
    prompt = f"""
    You are an expert Supply Chain Communication AI. Based on the following raw operational context, 
    draft a precise, legally sound, and highly impactful vendor email. 
    The tone must be {tone}. Do not include greetings like 'Dear User' or markdown notes. 
    Just return the subject line and the body of the email.

    Operational Context:
    {context_data}
    """
    
    # Utilizing the latest recommended Interactions API and gemini-3.8-flash model
    interaction = client.interactions.create(
        model='gemini-3.8-flash',
        input=prompt,
    )
    
    # Returning the generated text using the updated output_text interface
    return interaction.output_text.strip()

if __name__ == "__main__":
    # Real-world operational supply chain crisis scenario for testing
    sample_scm_crisis = """
    Scenario: Shipping Delay from Shanghai Port.
    Vendor Name: OceanFreight Global Ltd.
    Purchase Order (PO) Number: PO-2026-88302
    Issue: 40ft container containing critical electronic components is delayed by 7 days due to port congestion.
    Required Action: Demand immediate recovery plan and daily transit tracking updates. Warn them about potential late delivery penalties as per the contract SLA.
    """
    
    print("[*] Launching SCM Silicon Communication Engine with Gemini 3.8 Flash...")
    generated_email = generate_vendor_email_via_ai(sample_scm_crisis, tone="assertive and professional")
    
    print("\n=================== GENERATED OUTPUT ===================\n")
    print(generated_email)
    print("\n========================================================")
