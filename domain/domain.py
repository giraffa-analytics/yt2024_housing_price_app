from pydantic import BaseModel, Field

class ApiRequest(BaseModel):
    size: int = Field(default=0, description = "The size of the apartment in square meters.")
    year_built: int = Field(description = "The year the building was constructed.")
    bathrooms: int = Field(default=1, description = "The number of bathroom.")

class ApiResponse(BaseModel):
    price: int = Field(description = "The predicted price of the apartment.")