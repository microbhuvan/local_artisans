from __future__ import annotations

from typing import Optional, Tuple, Dict
from ..schemas import MarketingPlan, ChannelPlan
from ..config import settings


class AIProvider:
    async def generate_marketing_plan(
        self,
        *,
        description: str,
        title: str,
        category: Optional[str],
        price_range: Optional[str],
        region: Optional[str],
        image_bytes: Optional[bytes],
        image_filename: Optional[str],
    ) -> Tuple[MarketingPlan, Dict]:
        raise NotImplementedError


class MockProvider(AIProvider):
    async def generate_marketing_plan(
        self,
        *,
        description: str,
        title: str,
        category: Optional[str],
        price_range: Optional[str],
        region: Optional[str],
        image_bytes: Optional[bytes],
        image_filename: Optional[str],
    ) -> Tuple[MarketingPlan, Dict]:
        plan = MarketingPlan(
            productSummary=f"{title} — {category or 'handmade product'} for {region or 'local market'}",
            channels=[
                ChannelPlan(
                    channel="Instagram Reels",
                    why="Strong visual discovery for crafts",
                    target="18-35 in your city",
                    example_post="30s making-of clip with call-to-action to DM/order",
                    cadence="3x/week",
                    budget_pct=40,
                ),
                ChannelPlan(
                    channel="WhatsApp Communities",
                    why="Local trust and referrals",
                    target="Neighborhood groups",
                    example_post="Single image + price + pickup/delivery details",
                    cadence="2x/week",
                    budget_pct=20,
                ),
                ChannelPlan(
                    channel="Facebook Marketplace",
                    why="Local buyers searching handcrafted items",
                    target="City within 20km",
                    example_post="Gallery + clear pricing + custom options",
                    cadence="Weekly refresh",
                    budget_pct=20,
                ),
                ChannelPlan(
                    channel="Etsy",
                    why="Global reach for niche crafts",
                    target="Niche collectors",
                    example_post="Polished product photos + materials and story",
                    cadence="Bi-weekly",
                    budget_pct=20,
                ),
            ],
            contentIdeas=[
                "Before/after process shots",
                "Customer testimonial with photo",
                "Limited-time drop with countdown",
            ],
            hashtags=["#handmade", "#shopsmall", "#supportlocal"],
            geoTargets=[region or "your city"],
            influencerStrategy="Micro-influencers (2-10k) in crafts/home decor; offer barter",
            budgetTotalUsd=100,
            timeline=[
                "Week 1: Set up profiles and starter content",
                "Week 2: First drop, 3 reels, 1 marketplace listing",
                "Week 3: Testimonials + WhatsApp push",
            ],
            analytics=["Reach", "Saves", "DMs", "Conversion rate"],
            risks=["Inconsistent posting", "Low-quality photos"],
        )
        meta = {"provider": "mock", "tokensUsed": 0, "costEstimate": 0.0}
        return plan, meta


def get_ai_provider() -> AIProvider:
    # For now only mock; later switch based on settings.ai_provider
    return MockProvider()


