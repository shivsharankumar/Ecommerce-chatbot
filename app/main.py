"""
Retimer Bot - An Intelligent Chatbot System

This module implements a Streamlit-based chatbot that can handle different types of queries
through semantic routing. It supports FAQ responses, SQL queries, and casual conversation.

Author: [Your Name]
Date: [Current Date]
"""

import streamlit as st
from typing import Dict, List, Optional
from pathlib import Path
import logging
import torch
from faq import ingest_faq_data, faq_chain
from sql import sql_chain
from smalltalk import talk
from router import semantics_router

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Fix torch classes path issue
torch.classes.__path__ = []

# Constants
FAQ_DATA_PATH = Path(__file__).parent / "resources/accordion_data.csv"

class ChatMessage:
    """Represents a chat message with role and content."""
    def __init__(self, role: str, content: str):
        self.role = role
        self.content = content

    def to_dict(self) -> Dict[str, str]:
        """Convert message to dictionary format."""
        return {"role": self.role, "content": self.content}

def initialize_session_state() -> None:
    """Initialize Streamlit session state variables."""
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

def process_query(query: str) -> str:
    """
    Process user query and route it to appropriate handler.
    
    Args:
        query (str): User's input query
        
    Returns:
        str: Response from the appropriate handler
        
    Raises:
        Exception: If routing or processing fails
    """
    try:
        route = semantics_router(query).name
        logger.info(f"Query routed to: {route}")
        
        handlers = {
            'faq': faq_chain,
            'sql': sql_chain,
            'small-talk': talk
        }
        
        if route in handlers:
            return handlers[route](query)
        else:
            logger.warning(f"Unimplemented route: {route}")
            return f"Route {route} not implemented yet"
            
    except Exception as e:
        logger.error(f"Error processing query: {str(e)}")
        return "I apologize, but I encountered an error processing your request. Please try again."

def display_chat_history(messages: List[Dict[str, str]]) -> None:
    """Display the chat history in the Streamlit interface."""
    for message in messages:
        with st.chat_message(message['role']):
            st.markdown(message['content'])

def main() -> None:
    """Main application entry point."""
    try:
        # Initialize FAQ data
        ingest_faq_data(FAQ_DATA_PATH)
        
        # Set up the Streamlit interface
        st.title("Retimer Bot")
        st.markdown("""
        Welcome to Retimer Bot! I can help you with:
        - Answering FAQs
        - Processing SQL queries
        - Engaging in casual conversation
        """)
        
        # Initialize session state
        initialize_session_state()
        
        # Display chat history
        display_chat_history(st.session_state.messages)
        
        # Get user input
        query = st.chat_input("How can I help you today?")
        
        if query:
            # Display user message
            with st.chat_message("user"):
                st.markdown(query)
            st.session_state.messages.append(ChatMessage("user", query).to_dict())
            
            # Process and display response
            response = process_query(query)
            with st.chat_message("assistant"):
                st.markdown(response)
            st.session_state.messages.append(ChatMessage("assistant", response).to_dict())
            
    except Exception as e:
        logger.error(f"Application error: {str(e)}")
        st.error("An unexpected error occurred. Please try refreshing the page.")

if __name__ == "__main__":
    main()


