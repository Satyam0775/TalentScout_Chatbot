# prompts.py

# Greeting message for candidates
greeting_prompt = """
<div style='
    background-color: #f9fbff;
    color: #222;
    padding: 20px;
    border-radius: 15px;
    margin: 20px auto;
    max-width: 600px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.2);
    font-size: 16px;
    line-height: 1.6;
'>
    <strong style="color:#111;">Welcome!</strong> 👋 I'm <b>TalentScout Assistant</b>.<br>
    I’ll guide you through the first step of the hiring process by collecting your details and 
    asking you some technical questions.<br><br>
    Click <strong>Begin</strong> to start!
</div>
"""

# Candidate information collection prompt
info_collection_prompt = """
<div style='
    background-color: #fff7e6;
    color: #222;
    padding: 20px;
    border-radius: 15px;
    margin: 20px auto;
    max-width: 600px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.1);
    font-size: 16px;
    line-height: 1.6;
'>
    <strong style="color:#111;">Please share the following details:</strong><br><br>
    <ul style='padding-left: 20px; color:#333;'>
        <li>Full Name</li>
        <li>Email Address</li>
        <li>Phone Number</li>
        <li>Years of Experience</li>
        <li>Current Location</li>
        <li>Desired Position</li>
    </ul>
</div>
"""

# Tech stack collection prompt
tech_stack_prompt = """
<div style='
    background-color: #eaf9f6;
    color: #222;
    padding: 20px;
    border-radius: 15px;
    margin: 20px auto;
    max-width: 600px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.1);
    font-size: 16px;
    line-height: 1.6;
'>
    <strong style="color:#111;">Next step:</strong> Tell me about your <b>technical skills</b>.<br>
    You may include:
    <ul style='padding-left: 20px; margin-top: 5px; color:#333;'>
        <li>Programming Languages</li>
        <li>Frameworks & Libraries</li>
        <li>Databases</li>
        <li>Cloud Platforms</li>
        <li>Other Tools & Technologies</li>
    </ul>
</div>
"""

# Dynamic prompt for technical questions
def dynamic_generation_prompt(tech: str, level: str = "intermediate"):
    return (
        f"Generate 3 to 5 {level}-level technical interview questions "
        f"to test a candidate's proficiency in: {tech}. "
        f"Keep questions clear, concise, and job-relevant."
    )

# Fallback response
fallback_response = "I’m not sure I understood that. Could you rephrase? 🙂"

# Exit flow
exit_message = (
    "✅ Thanks for your time! Our recruitment team will review your information "
    "and reach out to you shortly."
)

exit_keywords = ["exit", "quit", "end", "stop", "thank you", "bye", "close"]
