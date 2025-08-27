from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi import status
from typing import Optional
import json

from ..schemas import AnalyzePayload, AnalyzeResponse, MarketingPlan, ChannelPlan
from ..services.ai_provider import get_ai_provider


router = APIRouter(tags=["analyze"])


@router.post("/analyze-product", response_model=AnalyzeResponse)
async def analyze_product(
    image: Optional[UploadFile] = File(default=None),
    payload: str = Form(...),
):
    try:
        payload_obj = AnalyzePayload(**json.loads(payload))
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Invalid payload: {exc}")

    ai = get_ai_provider()

    # For MVP we do not persist the file. If present, we read a small sample to confirm it's okay.
    image_bytes: Optional[bytes] = None
    image_url: Optional[str] = None
    if image is not None:
        image_bytes = await image.read()
        # In a real app, upload to S3/R2 and set image_url
        image_url = None

    plan, meta = await ai.generate_marketing_plan(
        description=payload_obj.description,
        title=payload_obj.title,
        category=payload_obj.category,
        price_range=payload_obj.priceRange,
        region=payload_obj.region,
        image_bytes=image_bytes,
        image_filename=image.filename if image is not None else None,
    )

    return AnalyzeResponse(
        plan=plan,
        imageUrl=image_url,
        provider=meta.get("provider", "mock"),
        tokensUsed=meta.get("tokensUsed"),
        costEstimate=meta.get("costEstimate"),
    )


