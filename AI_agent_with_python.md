🧠 Project: Build Your Own AI Chatbot with Groq API! 🤖

![Groq Logo](https://cdn.asp.events/CLIENT_Informa__AADDE28D_5056_B739_5481D63BF875B0DF/sites/ai-summit-NY-2022/media/libraries/exhibitors/0b84f0a6-3bbd-11ee-bff906bd0f937899-cover-image.png/fit-in/1500x9999/filters\:no_upscale\(\))

Welcome, Future AI Engineers! 🚀
In this project, you’ll bring **artificial intelligence to life** by creating a chatbot powered by the **Groq API** using Python’s `requests` module. You’ll practice calling external APIs, handling JSON, and making your terminal a chat interface to the future.

---

## **💡 Why This Project?**

By the end of this project, you’ll:
✅ Understand and implement real API calls in Python
✅ Learn how to structure and handle JSON data
✅ Build a working, real-time chatbot powered by **LLaMA 3**
✅ Strengthen your coding skills through real-world application

---

## **🛠️ Step 1: Get Your API Key**

1. Go to **[Groq’s official website](https://groq.com/)** and create an account
2. Access the **Groq Console** and generate your **API key**
3. Copy your API key and keep it safe—you’ll paste it into the script

---

## **🖥️ Step 2: Build Your AI Chatbot**

Replace `'YOUR_API_KEY_HERE'` with your personal API key, then **fill in the missing parts** to complete the script:

```python
import requests

# === Configuration ===
API_KEY = "YOUR_API_KEY_HERE"  # TODO: Paste your API key here
API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "llama3-8b-8192"

# === Chat Function ===
def get_ai_response(user_input):
    headers = {
        "Authorization": f"Bearer {_____}",  # TODO: Use your API key
        "Content-Type": "application/json"
    }

    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    }

    try:
        # Send the POST request to the Groq API
        response = requests._____(_____, headers=_____, json=_____)  # TODO: Complete this line
        response.raise_for_status()  # Ensure no HTTP errors
        result = response.____()  # TODO: Extract JSON content
        return result["choices"][0]["message"]["_____"]  # TODO: Get AI's message
    except Exception as e:
        return f"Error: {e}"

# === Main Chat Loop ===
if __name__ == "__main__":
    print("🤖 Welcome to your Groq-powered AI chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye! 👋")
            break
        reply = get_ai_response(user_input)
        print("AI:", reply)
```

---

## **🔧 Extra Challenges (Optional but Fun!)**

✨ Add chat history logging to a text file
✨ Let users change the system prompt to modify AI personality
✨ Switch between Groq models (e.g., `llama3-70b-8192`)
✨ Add GUI with `tkinter` or a web version with `Flask`

---

## **📌 Helpful Resources**

🔗 [Groq API Docs](https://console.groq.com/docs/quickstart)
📘 [Python Requests Docs](https://docs.python-requests.org/en/latest/)
🐍 [Python Official Docs](https://docs.python.org/3/)

---

## **🎯 Grading Criteria**

| Feature                             | Points |
| ----------------------------------- | ------ |
| Proper API key usage and connection | ✅ 30   |
| Error handling with `try/except`    | ✅ 20   |
| Function-based chatbot logic        | ✅ 20   |
| Extra features (GUI, logging, etc.) | ✅ 30   |

---

## **🎉 Ready? Let’s Build AI! 🚀**

This project gives you real-world practice working with AI APIs. Whether for your portfolio, job prep, or just geeky fun—this is your gateway to **next-gen software development**.
