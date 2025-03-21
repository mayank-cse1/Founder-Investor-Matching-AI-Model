from pydantic import BaseModel, Field, conint
from typing import Dict

# Define Weights for different matching criteria
WEIGHTS: Dict[str, int] = {
    "industry_match": 20,
    "investment_fit": 10,
    "startup_stage_alignment": 15,
    "previous_investment_preferences": 15,
    "market_trends": 5,
    "geographical_alignment": 5,
    "founder_experience": 15,
}

# Individual Criteria Models
class IndustryMatch(BaseModel):
    industry_match: conint(ge=0, le=10)
    reason: str

class InvestmentFit(BaseModel):
    investment_fit: conint(ge=0, le=10)
    reason: str

class StartupStageAlignment(BaseModel):
    startup_stage_alignment: conint(ge=0, le=10)
    reason: str

class PreviousInvestments(BaseModel):
    previous_investments: conint(ge=0, le=10)
    reason: str

class MarketTrends(BaseModel):
    market_trends: conint(ge=0, le=10)
    reason: str

class GeographicalAlignment(BaseModel):
    geographical_alignment: conint(ge=0, le=10)
    reason: str

class FounderExperience(BaseModel):
    founder_experience: conint(ge=0, le=10)
    reason: str

# Aggregated Criteria Model
class Criteria(BaseModel):
    industry_match: IndustryMatch
    investment_fit: InvestmentFit
    startup_stage_alignment: StartupStageAlignment
    previous_investments: PreviousInvestments
    market_trends: MarketTrends
    geographical_alignment: GeographicalAlignment
    founder_experience: FounderExperience

# Match Score Model
class MatchScore(BaseModel):
    investor_id: str
    founder_id: str
    rating: conint(ge=0, le=10)
    criteria_for_rating: Criteria
    explanation_for_rating: str
    suggestion_for_founder: str