from pydantic import BaseModel, Field
from typing import List, Optional


class ChannelPlan(BaseModel):
    channel: str
    why: str
    target: str
    example_post: str
    cadence: str
    budget_pct: int = Field(ge=0, le=100)


class MarketingPlan(BaseModel):
    productSummary: str
    channels: List[ChannelPlan]
    contentIdeas: List[str]
    hashtags: List[str]
    geoTargets: List[str]
    influencerStrategy: str
    budgetTotalUsd: Optional[int] = None
    timeline: List[str]
    analytics: List[str]
    risks: List[str]


class AnalyzePayload(BaseModel):
    title: str
    description: str
    category: Optional[str] = None
    priceRange: Optional[str] = None
    region: Optional[str] = None


class AnalyzeResponse(BaseModel):
    plan: MarketingPlan
    imageUrl: Optional[str] = None
    provider: str
    tokensUsed: Optional[int] = None
    costEstimate: Optional[float] = None


