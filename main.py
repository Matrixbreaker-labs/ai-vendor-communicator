import os
from google import genai

# ১. সাপ্লাই চেইন ইমেইল অপটিমাইজেশন ইঞ্জিন (SCM Email Optimization Engine)
def generate_vendor_email_via_ai(context_data, tone="professional"):
    """গুগল জেমিনি এপিআই ব্যবহার করে সাপ্লাই চেইনের জটিল পরিস্থিতি অনুযায়ী অটোমেটিক ইমেইল ড্রাফট করার মেকানিズム।"""
    client = genai.Client()
    
    prompt = f"""
    You are an expert Supply Chain Communication AI. Based on the following raw operational context, 
    draft a precise, legally sound, and highly impactful vendor email. 
    The tone must be {tone}. Do not include greetings like 'Dear User' or markdown notes. 
    Just return the subject line and the body of the email.

    Operational Context:
    {context_data}
    """
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
    )
    return response.text.strip()

if __name__ == "__main__":
    # টেস্ট করার জন্য একটি রিয়াল-ওয়ার্ল্ড সাপ্লাই চেইন ডিলে সিনারিও
    sample_scm_crisis = """
    Scenario: Shipping Delay from Shanghai Port.
    Vendor Name: OceanFreight Global Ltd.
    Purchase Order (PO) Number: PO-2026-88302
    Issue: 40ft container containing critical electronic components is delayed by 7 days due to port congestion.
    Required Action: Demand immediate recovery plan and daily transit tracking updates. Warn them about potential late delivery penalties as per the contract SLA.
    """
    
    print("[*] Launching SCM Silicon Communication Engine...")
    generated_email = generate_vendor_email_via_ai(sample_scm_crisis, tone="assertive and professional")
    
    print("\n=================== GENERATED OUTPUT ===================\n")
    print(generated_email)
    print("\n========================================================")
