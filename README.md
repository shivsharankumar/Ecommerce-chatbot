# Retimer Bot 🤖

An intelligent chatbot system built with Streamlit that uses semantic routing to handle different types of queries including FAQs, SQL queries, and casual conversation.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.45.1-FF4B4B)
![License](https://img.shields.io/badge/License-MIT-green)

## 🌟 Features

- **Semantic Query Routing**: Intelligently routes user queries to appropriate handlers
- **FAQ Management**: Handles frequently asked questions with accurate responses
- **SQL Query Processing**: Processes and executes SQL queries
- **Natural Conversation**: Engages in casual conversation using advanced NLP
- **Real-time Chat Interface**: Modern and responsive chat UI using Streamlit
- **Error Handling**: Robust error handling and logging system
- **Session Management**: Maintains chat history during user sessions

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/shivsharankumar/Ecommerce-chatbot.git
cd retimer-bot
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
streamlit run app/main.py
```

The application will be available at `http://localhost:8501`

## 🛠️ Project Structure

```
retimer-bot/
├── app/
│   ├── main.py              # Main application entry point
│   ├── faq.py              # FAQ handling module
│   ├── sql.py              # SQL query processing
│   ├── smalltalk.py        # Casual conversation handling
│   └── router.py           # Semantic routing logic
├── resources/
│   └── accordion_data.csv  # FAQ data
├── requirements.txt        # Project dependencies
└── README.md              # Project documentation
```

## 💡 Usage

1. Open the application in your web browser
2. Type your query in the chat input
3. The bot will automatically:
   - Route your query to the appropriate handler
   - Process your request
   - Provide a relevant response

### Example Queries

- FAQ: "What are your business hours?"
- SQL: "Show me the sales data for last month"
- Casual: "How are you today?"

## 🔧 Technical Details

### Key Technologies

- **Streamlit**: Web application framework
- **Python**: Core programming language
- **Semantic Routing**: Intelligent query classification
- **NLP**: Natural Language Processing for conversation
- **SQL**: Database query processing

### Architecture

The application uses a modular architecture with the following components:

1. **Semantic Router**: Classifies incoming queries
2. **Query Handlers**: Process specific types of queries
3. **Chat Interface**: Manages user interaction
4. **Session Management**: Maintains conversation state

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- Your Name - Shiv Sharan Kumar

## 🙏 Acknowledgments

- Thanks to all contributors who have helped shape this project
- Inspired by modern chatbot architectures
- Built with Streamlit's amazing framework

## 📞 Support

For support, please open an issue in the GitHub repository or contact [shivsharan47@gmail.com]

---

⭐️ If you like this project, please give it a star on GitHub!
