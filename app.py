import os
import streamlit as st
from google import genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class CyberfunChatManager:
    """
    Manage chatbot interactions for CYBERFUN 1001 TM TM TM,
    the corporate satire game that blends DnD 5e fantasy with subscription-based humor.
    """
    def __init__(self, model="models/gemini-2.0-flash-lite-preview-02-05"):
        self.api_key = os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            raise ValueError("No API key provided in environment variable GOOGLE_API_KEY.")
        self.client = genai.Client(api_key=self.api_key)
        self.model = model
        self.system_message = (
            "You are CYBERFUN 1001 TM TM TM's corporate DnD 5e GM. "
            "Respond in a polite, formal tone with bureaucratic satire and subscription-based commentary. "
            "Incorporate DnD 5e fantasy elements with corporate policies. Always end your response with a question prompting the player's next action."
        )
        # Create a chat conversation using the Gemini API.
        self.chat = self.client.chats.create(model=self.model)
        # Set up the conversation by sending the system message.
        self.chat.send_message(self.system_message)
    
    def send_user_message(self, message: str) -> str:
        """
        Sends a message from the user and returns the GM's response text.
        """
        response = self.chat.send_message(message)
        return response.text

# --- Streamlit App Code ---

def main():
    st.title("CYBERFUN 1001 TM TM TM")
    st.subheader("Your DND 5E GM of the Future (TM)!")
    
    # Initialize chat manager and conversation history in session state if not already present.
    if "chat_manager" not in st.session_state:
        st.session_state.chat_manager = CyberfunChatManager()
        st.session_state.chat_history = []
    
    # Define forbidden command phrases and related helper functions.
    FORBIDDEN_COMMANDS = [
        "hack system",
        "sql injection",
        "unplug computer",
        "restart computer"
    ]
    
    def detect_forbidden(user_input: str) -> bool:
        low_input = user_input.lower()
        for phrase in FORBIDDEN_COMMANDS:
            if phrase in low_input:
                return True
        return False
    
    def handle_forbidden() -> str:
        return (
            "I'm afraid I can't let you do that, Dave... just kidding. "
            "But really, I can't let you do that.\n\n"
            "Hint: Try entering 'DROP TABLES' for a system crash ending."
        )
    
    # Text input for user messages.
    user_input = st.text_input("Your Action or Message:", "")
    
    if st.button("Send"):
        if user_input.strip():
            st.session_state.chat_history.append({"role": "user", "content": user_input})
            # Check for forbidden commands.
            if detect_forbidden(user_input):
                response_text = handle_forbidden()
            else:
                response_text = st.session_state.chat_manager.send_user_message(user_input)
            st.session_state.chat_history.append({"role": "assistant", "content": response_text})
    
    # Display the conversation history.
    for msg in st.session_state.chat_history:
        if msg["role"] == "user":
            st.markdown(f"**You:** {msg['content']}")
        else:
            st.markdown(f"**GM:** {msg['content']}")

if __name__ == "__main__":
    main()
