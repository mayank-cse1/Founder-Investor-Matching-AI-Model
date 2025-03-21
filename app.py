from flask import Flask, request, jsonify
import pandas as pd
from services import get_match_score, compute_final_score, get_summary
import time
app = Flask(__name__)

@app.route('/match_founders', methods=['POST'])
def match_founders():
    """ API Endpoint to match investors with founders """
    data = request.get_json()

    founder_df = pd.DataFrame(data["founders"])
    investor_df = pd.DataFrame(data["investors"])

    founders_info = {row['Founder_ID']: row.to_dict() for _, row in founder_df.iterrows()}
    investors_info = {row['Investor_ID']: row.to_dict() for _, row in investor_df.iterrows()}

    match_scores = []
    for investor_id, investor_data in investors_info.items():
        for founder_id, founder_data in founders_info.items():
            match_score = get_match_score(investor_id, investor_data, founder_id, founder_data)
            match_score['rating'] = compute_final_score(match_score['criteria_for_rating'])
            match_scores.append(match_score)
            time.sleep(1)

    # Sort by rating in descending order
    match_scores.sort(key=lambda x: x['rating'], reverse=True)
    
    text_response = get_summary(founder_data, match_scores[0])
    return jsonify({"match_scores": match_scores, "text_response": text_response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
