import os
import streamlit as st
from google import genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the Gemini API client with your API key
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# Define forbidden commands
FORBIDDEN_COMMANDS = [
    "hack system",
    "sql injection",
    "unplug computer",
    "restart computer"
]

def detect_forbidden(user_input: str) -> bool:
    """Check if the user's input contains any forbidden command phrases."""
    low_input = user_input.lower()
    for phrase in FORBIDDEN_COMMANDS:
        if phrase in low_input:
            return True
    return False

def handle_forbidden() -> str:
    """Return the DM's response when a forbidden command is detected."""
    return (
        "I'm afraid I can't let you do that, Dave... just kidding. "
        "But really, I can't let you do that.\n\n"
        "Hint: Try entering 'DROP TABLES' for a system crash ending."
    )

def main():
    st.title("CYBERFUN 1001 TM TM TM")
    st.subheader("Your DND 5E GM of the Future (TM)!")

    # Initialize chat and conversation history in session state
    if "chat" not in st.session_state:
        # Create a chat conversation using your chosen Gemini model
        st.session_state.chat = client.chats.create(model="models/gemini-2.0-flash-lite-preview-02-05")
        st.session_state.conversation = []
        # Optional: add an initial system instruction (for display purposes)
        system_message = (
            "You are CYBERFUN 1001 TM TM TM's corporate DnD 5e GM. Respond in a polite, formal tone with "
            "bureaucratic satire and subscription-based commentary. Incorporate DnD 5e fantasy elements with "
            "corporate policies. Always end your response with a question prompting the player's next action."
        )
        st.session_state.conversation.append({"role": "system", "content": system_message})

    # Input field for user messages
    user_input = st.text_input("Your Action or Message:", "")

    if st.button("Send"):
        if user_input.strip():
            # Check for forbidden commands
            if detect_forbidden(user_input):
                st.session_state.conversation.append({"role": "user", "content": user_input})
                st.session_state.conversation.append({"role": "assistant", "content": handle_forbidden()})
            else:
                st.session_state.conversation.append({"role": "user", "content": user_input})
                # Send the user's message to the Gemini chat API
                response = st.session_state.chat.send_message(user_input)
                response_text = response.text  # the response object has a .text attribute
                st.session_state.conversation.append({"role": "assistant", "content": response_text})

    # Display the conversation history
    for msg in st.session_state.conversation:
        if msg["role"] == "user":
            st.markdown(f"**You:** {msg['content']}")
        elif msg["role"] == "assistant":
            st.markdown(f"**GM:** {msg['content']}")
        else:
            st.markdown(f"*{msg['content']}*")

if __name__ == "__main__":
    main()
