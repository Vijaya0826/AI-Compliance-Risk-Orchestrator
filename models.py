from typing import Dict, Any, List, Literal
from pydantic import BaseModel
from datetime import datetime

class Citation(BaseModel):
    doc_id: str
    chunk_id: str
    snippet: str

class HumanInteraction(BaseModel):
    timestamp: datetime
    type: Literal["clarification", "approval", "upload_request"]
    prompt: str
    response: str
    status: Literal["approved", "denied", "provided", "timeout"]

class ComplianceResult(BaseModel):
    decision: Literal["compliant", "non_compliant", "insufficient_evidence"]
    confidence: float
    risk_score: float
    rationale: str
    citations: List[Citation]
    open_questions: List[str]
    human_interactions: List[HumanInteraction]

class AskRequest(BaseModel):
    question: str
    attachments: Dict[str, Any] = None
