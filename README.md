 **AI Company Research Assistant**

The **AI Company Research Assistant** is a streamlined, enterprise-focused intelligence system designed to conduct **real-time company research** using multiple live data sources including **Yahoo Finance**, **Google News**, **Wikipedia**, and **Gemini AI**.  

It generates a **professional Account Plan**, updates specific sections via user input, and supports conversational interactions — all through a clean and intuitive Streamlit interface.

## Key Capabilities

###  Real-time Company Research  
Automatically aggregates information from:
- Yahoo Finance (Industry, Market Cap, Key Stats)
- Google News RSS (Latest Headlines)
- Wikipedia (Summary + History)
- Gemini LLM (Data interpretation + Plan generation)

### Account Plan Generator  
Creates **8 structured business sections**:
- Company Overview  
- Products & Services  
- Market Position  
- Competitors  
- Recent News  
- Opportunities  
- Risks  
- Final Summary 

### Interactive Plan Editing  
Users can update specific sections via simple instructions: 

###  Off-topic Detection  
Rejects non-business or unrelated questions gracefully:
> “I can only answer company-related research queries.”

###  Business Chat Responses  
If a query is related to business or analysis (but not a company name), it responds using the Gemini model.

### Project Folder Structure
```
AI_Assistant/
│── app.py                     # Main Streamlit Application
│
│── core/
│   │── llm_client.py          # Gemini API wrapper
│   │── ticker_service.py      # Yahoo Search ticker finder
│   │── yahoo_service.py       # Yahoo Finance extractor
│   │── news_service.py        # Google News RSS fetcher
│   │── wiki_service.py        # Wikipedia data scraper
│   │── research_engine.py     # Orchestrates all services
│
│── plan/
│   │── plan_generator.py      # Multi-section account plan generator
│   │── plan_updater.py        # Section updater module
│
│── ui/
│   │── layout.py              # Header, chat, sidebar layout
│   │── theme.py               # Global UI theming
│   │── components.py          # Buttons, input box, reusable UI parts
│   │── assets/
│       │── bot_avatar.png     # Assistant avatar
│
│── utils/
│   │── logger.py              # Debug logging
│   │── text_cleaner.py        # Cleaning & formatting utilities
│
│── config/
│   │── keys.env               # GEMINI_API_KEY stored here
```


### System Architecture
```
┌────────────────────────────────────────────────────────┐
│                    User Interface                       │
│                (Streamlit Frontend)                     │
└────────────────────────────────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│                    Research Engine                      │
│               (core/research_engine.py)                 │
└────────────────────────────────────────────────────────┘
           │                         │
           ▼                         ▼
 ┌─────────────────┐        ┌────────────────────┐
 │   TickerFinder   │        │    WikiFetcher     │
 │ (Yahoo Ticker)   │        │ (Wikipedia API)    │
 └─────────────────┘        └────────────────────┘
           │                         │
           ▼                         ▼
 ┌─────────────────┐        ┌────────────────────┐
 │  Yahoo Search    │        │ Google News RSS    │
 │ (Company Data)   │        │ Latest Headlines   │
 └─────────────────┘        └────────────────────┘
           │                         │
           └──────────────┬──────────┘
                          ▼
                ┌────────────────────┐
                │     Gemini LLM     │
                │ (Plan Generation)  │
                └────────────────────┘
                          ▼
                ┌────────────────────┐
                │  Account Plan (8)  │
                └────────────────────┘
```



#  Data Flow Overview
```
User Input
│
▼
ResearchEngine.run()
├── TickerFinder → ticker
├── YahooData → financials
├── NewsFetcher → headlines
├── WikiFetcher → summary + history
└── LLM Fallback (if needed)
│
▼
PlanGenerator.generate()
└── Gemini LLM produces 8-section plan
│
▼
Rendered in Sidebar
│
▼
User updates → PlanUpdater
```



#  How the Application Works (Step-by-Step)

### 1️ User enters a company name  
Example:  tesla


### 2️ Research Engine executes  
- Searches Yahoo for ticker ("TSLA")  
- Fetches profile via Yahoo Finance  
- Fetches related news via Google News  
- Fetches Wikipedia summary  
- Cleans and structures all data  

### 3️ Gemini generates the Account Plan  
Using all combined data, Gemini produces:

- Company Overview  
- Products & Services  
- Market Position  
- Competitors  
- Recent News  
- Opportunities  
- Risks  
- Final Summary  

### 4️ Sidebar updates with the final plan  
Fully structured and readable.

### 5️ User may update specific sections  
update risks


---

#  Technology Stack

### **Frontend**
- Streamlit  
- Custom CSS  
  

### **Backend**
- Python 3.12  
- yfinance  
- Google News RSS  
- Wikipedia API  
- Gemini API  

### **AI Model**
- Gemini 2.0 Flash   

Used for:
- Business reasoning  
- Account plan generation  
- Company search fallback  
- Natural-language analysis  

---

#  Installation & Setup

### 1. Clone Repository

git clone <repo-url>
cd Project_AI_AGENT

### 2 Install Dependencies

pip install -r requirements.txt

### 3 Add API Keys

Create:

config/keys.env

Add:

GEMINI_API_KEY=your_api_key_here

###  4. Run App

streamlit run app.py

### Conclusion

This AI Company Research Assistant delivers a full enterprise-ready workflow by integrating:

Multi-source real-time data retrieval

AI-driven reasoning

Professional account plan creation

Conversational intelligence

Modern, clean user experience

APPLICATION SCREEN SHOT 

<img width="2877" height="1493" alt="image" src="https://github.com/user-attachments/assets/5b6e055f-ef77-4635-8616-fdf60dbc13d2" />




