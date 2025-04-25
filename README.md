# Lead Intelligence Pipeline 🚀

This project automates the lead qualification pipeline using GPT-4 for classification and enrichment. It integrates with CRM systems (Kommo, Supabase) and is orchestrated through n8n for workflow automation.

## 🔍 Objective
Automate the extraction, enrichment, classification, and CRM integration of leads coming from channels like WhatsApp, web forms, or chatbots.

## 🧠 Features
- Uses OpenAI GPT-4 to extract and classify information from raw lead messages.
- Scores leads based on extracted data and intent.
- Sends structured data to Kommo CRM or Supabase.
- All orchestrated using `n8n` (low-code platform).

## ⚙️ Tech Stack
- Python 3.10+
- OpenAI GPT-4 (via `openai` lib)
- Redis + Supabase (mocked for demo)
- n8n
- JSON / API Integrations

## 🗂️ Structure
```
lead-intelligence-pipeline/
├── main.py                # Main Python script for lead processing
├── requirements.txt       # Required libraries
├── sample_input.txt       # Simulated lead input
├── assets/
│   ├── flow-diagram.png   # Flow chart image
│   └── crm-output-sample.json
└── README.md              # Project overview
```

## ✅ Outcome
- +70% sales team efficiency
- Less manual input into CRM
- Real-time scoring and categorization
