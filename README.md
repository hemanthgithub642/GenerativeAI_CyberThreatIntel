# Generative AI for Cyber Threat Intelligence

**Objective**: Leverage Generative AI to summarize and predict emerging cybersecurity threats using data from trusted sources.

## Project Overview
This project uses pre-trained generative models to analyze cybersecurity incident reports and predict trends in attack vectors. The system provides concise summaries and visualized insights, enabling proactive measures against cyber threats.

---

## Project Structure

```
GenerativeAI_CyberThreatIntel/
|
|-- data/             # Collected datasets (e.g., JSON, CSV)
|-- models/           # Pre-trained and fine-tuned AI models
|-- scripts/          # Python scripts for data processing and analysis
|-- dashboard/        # Streamlit dashboard code
|-- README.md         # Project documentation
|-- requirements.txt  # Python dependencies
```

---

## How to Run

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<your-username>/GenerativeAI_CyberThreatIntel.git
   cd GenerativeAI_CyberThreatIntel
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Dashboard**:
   ```bash
   streamlit run dashboard/main.py
   ```

---

## Tools Used

- **Generative AI**: Hugging Face Transformers (e.g., BART, GPT-2)
- **Data Sources**: MITRE ATT&CK, AlienVault OTX, cybersecurity RSS feeds
- **Visualization**: Streamlit, Matplotlib, Plotly

---

## Features

1. **Summarization**: Generates concise summaries of cybersecurity reports and news articles.
2. **Trend Analysis**: Predicts attack vectors and identifies recurring threats.
3. **Interactive Dashboard**: Visualizes summarized threats and trends interactively.

---

## Future Enhancements

- Fine-tune generative models with custom datasets.
- Add real-time threat detection and alerting capabilities.
- Incorporate Natural Language Understanding (NLU) for deeper analysis of unstructured data.

---


