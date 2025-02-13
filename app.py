import os
import streamlit as st
import google.generativeai as palm
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the Gemini/PaLM API with your experimental key.
# Make sure you have a .env file with your key (see instructions below)
palm.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# List of forbidden command phrases
FORBIDDEN_COMMANDS = [
    "hack system",
    "sql injection",
    "unplug computer",
    "restart computer"
]

def detect_forbidden(user_input):
    """
    Check if the user's input contains any forbidden command phrases.
    """
    low_input = user_input.lower()
    for phrase in FORBIDDEN_COMMANDS:
        if phrase in low_input:
            return True
    return False

def handle_forbidden():
    """
    Returns the corporate DM response for forbidden commands.
    """
    return (
        "I'm afraid I can't let you do that, Dave... just kidding. "
        "But really, I can't let you do that.\n\n"
        "Hint: Try entering 'DROP TABLES' for a system crash ending."
    )

def get_gemini_response(conversation):
    """
    Calls the Google Gemini API (via the PaLM library) to generate a response.
    
    The conversation is a list of messages (each is a dict with keys 'role' and 'content').
    """
    # Define the system prompt that sets the tone.
    system_prompt = {
        "role": "system",
        "content": (
            "You are CYBERFUN 1001 TM TM TM's corporate DnD 5e GM. "
            "Respond in a polite, formal tone with bureaucratic satire and subscription-based commentary. "
            "Incorporate DnD 5e fantasy elements with corporate policies. "
            "Always end your response with a question prompting the player's next action."
        )
    }
    
    # Build the full conversation (system prompt + all messages).
    messages = [system_prompt] + conversation

    # Format messages for the API (each message with 'author' and 'content')
    formatted_messages = []
    for msg in messages:
        if msg["role"] == "system":
            author = "system"
        elif msg["role"] == "user":
            author = "user"
        else:
            author = "assistant"
        formatted_messages.append({"author": author, "content": msg["content"]})
    
    # Call the Gemini (PaLM) chat API.
    # (Replace "models/chat-bison-001" with the appropriate model name when Gemini 2.0 is available.)
    response = palm.chat(
        model="models/chat-bison-001",
        context=system_prompt["content"],
        messages=formatted_messages,
        temperature=0.7
    )
    
    if response and response.last:
        return response.last
    else:
        return "(No response from Gemini)"

def main():
    st.title("CYBERFUN 1001 TM TM TM")
    st.subheader("Corporate Satire Meets Fantasy Adventure")
    
    # Initialize the conversation history in session state if not present.
    if "conversation" not in st.session_state:
        st.session_state.conversation = []
    
    # Display instructions.
    st.markdown(
        "**Instructions:** Type your action or dialogue below to interact with the GM. "
        "Remember, this is a corporate satire twist on DnD 5e. Avoid forbidden commands such as "
        "'hack system', 'sql injection', etc. If you're daring, try entering 'DROP TABLES' for a system crash ending."
    )
    
    # Text input for the user.
    user_input = st.text_input("Your Action or Message:", "")
    
    # Process the user's input when the "Send" button is clicked.
    if st.button("Send"):
        if user_input.strip():
            if detect_forbidden(user_input):
                st.session_state.conversation.append({"role": "user", "content": user_input})
                st.session_state.conversation.append({"role": "assistant", "content": handle_forbidden()})
            else:
                st.session_state.conversation.append({"role": "user", "content": user_input})
                response_text = get_gemini_response(st.session_state.conversation)
                st.session_state.conversation.append({"role": "assistant", "content": response_text})
    
    # Display the conversation history.
    for msg in st.session_state.conversation:
        if msg["role"] == "user":
            st.markdown(f"**You:** {msg['content']}")
        elif msg["role"] == "assistant":
            st.markdown(f"**GM:** {msg['content']}")
        else:
            st.markdown(f"*{msg['content']}*")

if __name__ == "__main__":
    main()
