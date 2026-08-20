"""FastAPI Backend Server."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="VAM Backend",
    description="Vector Asset Management Backend API",
    version="0.1.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def health_check():
    """Health check endpoint."""
    return JSONResponse(
        status_code=200,
        content={"status": "healthy", "service": "VAM Backend"}
    )


@app.get("/api/v1/health")
async def api_health():
    """API health endpoint."""
    return {
        "status": "ok",
        "version": "0.1.0",
        "service": "Vector Asset Management"
    }


@app.get("/api/v1/assets")
async def list_assets():
    """List all assets."""
    return {
        "assets": [],
        "total": 0,
        "message": "No assets found"
    }


@app.post("/api/v1/assets")
async def create_asset(name: str, description: str = ""):
    """Create a new asset."""
    return {
        "id": 1,
        "name": name,
        "description": description,
        "status": "created"
    }


@app.get("/api/v1/assets/{asset_id}")
async def get_asset(asset_id: int):
    """Get a specific asset."""
    return {
        "id": asset_id,
        "name": f"Asset {asset_id}",
        "description": "Sample asset",
        "created_at": "2026-08-20T18:00:00Z"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
