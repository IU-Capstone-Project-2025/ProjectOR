from fastapi import APIRouter

router = APIRouter(tags=["Health"])


@router.get("/health-check", summary="Health Check")
async def health_check():
    """
    Health check endpoint to verify the service is running.
    Returns a simple message indicating the service is healthy.
    """
    return {"status": "healthy"}
