from fastapi import FastAPI
from service.service import PriceEstimator
from domain.domain import ApiRequest, ApiResponse
import uvicorn

SERVER_HOST = "localhost"
SERVER_PORT = 8000

# Initialize the api
app = FastAPI()

@app.post("/estimate")
async def estimate_price(request:ApiRequest) -> ApiResponse:
    estimated_price = PriceEstimator().predict_price(request=request)
    return estimated_price

if __name__=="__main__":
    uvicorn.run(
        "main:app",
        host=SERVER_HOST,
        port=SERVER_PORT,
        reload=True # just for development usage - high consumer
    )