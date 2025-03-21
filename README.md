# Founder-Investor-Matching-AI-Model

## Objective
The **Founder-Investor Matching AI Model** is designed to help match startup founders with potential investors based on structured data. The model analyzes founder information and investor preferences to compute a compatibility score, providing ranked results.

## Features
- Uses **Gemini API** to process and analyze compatibility.
- Computes a **match score** between investors and founders.
- Returns a **ranked list of potential investors** based on compatibility.
- Ensures **seamless API integration** and proper response handling.

## Dataset
The model operates on a structured dataset containing:
### **Founder Information:**
- Industry
- Startup stage
- Funding required
- Traction
- Business model

### **Investor Preferences:**
- Preferred industry
- Investment range

## Tasks & Implementation
### **1. Model Implementation Using Gemini API**
- Integrate **Gemini API** to analyze compatibility between investors and founders.
- Handle API requests and responses efficiently to extract relevant insights.

### **2. Match Score Calculation**
- Process startup and investor data to compute a compatibility score.
- The score reflects how well an investor’s interests align with a startup’s profile.

### **3. Output Format**
- Returns a list of **investors matching the founder’s profile**.
- Displays **ranked results** in a structured format based on compatibility score.

## Installation & Usage
### **Prerequisites**
- Python 3.x
- API key for Gemini API

### **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/mayank-cse1/Founder-Investor-Matching-AI-Model.git
   cd Founder-Investor-Matching-AI-Model
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up **Gemini API Key** in your environment variables:
   ```bash
   export GEMINI_API_KEY='your-api-key-here'
   ```
### Folder Structure
/Founder-Investor-Matching-AI-Model
│── /data
│   ├── investor.csv
│   ├── founder.csv
│   ├── founder-investor-mapping-score.csv
│── app.py
│── models.py
│── services.py
│── ui.py
│── .env
│── requirements.txt

### **Running the Model**
Execute the script to match founders with investors:
```bash
python app.py
```
Execute the streamlit ui
```bash
streamlit run ui.py
```
## Example Output
```json
{
"founder_experience":{
"founder_experience":0
"reason":"The founder profile does not include specific details about the founder's prior experience."
}
"geographical_alignment":{
"geographical_alignment":0
"reason":"The investor profile does not mention any geographical investment preferences."
}
"industry_match":{
"industry_match":9
"reason":"The founder's company, PayFlowX, uses AI-driven analytics, which aligns with the investor's preferred industry of AI/ML and DeepTech."
}
"investment_fit":{
"investment_fit":10
"reason":"PayFlowX is seeking $10,000,000, which falls perfectly within the investor's preferred investment range of $2,000,000 - $10,000,000."
}
"market_trends":{
"market_trends":0
"reason":"The investor profile does not contain any information related to market trends, so this is rated as zero."
}
"previous_investments":{
"previous_investments":0
"reason":"Information about the investor's previous investments is not available, resulting in a zero score for this criterion."
}
"startup_stage_alignment":{
"reason":"PayFlowX is looking for a Seed B investment. The investor prefers Series B and Growth stage investments, showing strong alignment."
"startup_stage_alignment":8
}
}
```

## Contributing
Feel free to submit issues and pull requests to improve the model.

## License
This project is licensed under the MIT License.

---
**Author:** Mayank Gupta  
**Contact:** mayank.guptacse1@gmail.com

