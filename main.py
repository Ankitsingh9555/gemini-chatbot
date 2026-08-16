import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0.7
)

print("🤖 Chatbot: Hello! Ask me anything. (Type 'exit' to quit)")
print("-" * 50)

while True:
    user_prompt = input("\n📝 You: ").strip()
    
    if user_prompt.lower() in ['exit', 'quit', 'bye']:
        print("🤖 Chatbot: Goodbye! Have a great day!")
        break
    
    if not user_prompt:
        print("🤖 Chatbot: Please ask me something!")
        continue
    
    response = llm.invoke(user_prompt)
    if hasattr(response, 'content'):
        content = response.content
        # Extract text and remove metadata
        text_only = ""
        try:
            if isinstance(content, str):
                # Try to parse as JSON if it looks like a list
                if content.startswith('['):
                    import json
                    try:
                        parsed = json.loads(content)
                        if isinstance(parsed, list) and len(parsed) > 0:
                            text_only = parsed[0].get('text', '')
                    except:
                        text_only = content
                else:
                    text_only = content
            elif isinstance(content, list):
                # Direct list - extract text
                if len(content) > 0 and isinstance(content[0], dict):
                    text_only = content[0].get('text', '')
                else:
                    text_only = str(content)
            else:
                text_only = str(content)
        except:
            text_only = str(content)
        
        if text_only:
            print(f"🤖 Chatbot: {text_only}")
        else:
            print(f"🤖 Chatbot: I couldn't process that response.")
    else:
        print(f"🤖 Chatbot: {str(response)}")

