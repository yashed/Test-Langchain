from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import lanchain_helpr as lh
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),  # Log to console
    ],
)

logger = logging.getLogger(__name__)

# Create FastAPI instance
app = FastAPI()

logger.info("Starting the FastAPI application")

# Enable CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
logger.info("CORS middleware enabled with all origins allowed")


# Define the request body schema using Pydantic
class UserRequest(BaseModel):
    name: str
    company: str
    country: str
    position: str
    interest: str


logger.info("UserRequest schema defined")


# Define root endpoint
@app.get("/")
async def read_root():
    logger.info("Root endpoint accessed")
    return {"message": "Welcome to the API"}


# Define a test endpoint
@app.get("/test")
def test_endpoint():
    logger.info("Test endpoint accessed")
    return {"message": "This is a test endpoint"}


# Define an endpoint
@app.post("/generate_data/")
async def generate_data(user: UserRequest):
    logger.info("Generate data endpoint called with user: %s", user.json())

    name = user.name
    company = user.company
    position = user.position
    country = user.country

    try:
        # Generate the data using the existing helper function
        logger.debug("Calling generate_data helper function with inputs")
        response = lh.generate_data(name, company, position, country)

        if not response:
            logger.error("Data generation failed for user: %s", user.json())
            raise HTTPException(status_code=404, detail="Data generation failed")

        logger.info("Data generation successful for user: %s", user.json())
        return {
            "professional_summary": response.get(
                "professional_summary", "No summary available"
            ),
            "social_media_links": response.get(
                "social_media_links", "No social media links found."
            ),
            "company_summary": response.get(
                "company_summary", "No company summary available"
            ),
            "company_competitors": response.get(
                "company_competitors", "No competitors found"
            ),
            "additional_insights": response.get(
                "additional_insights", "No additional insights available."
            ),
        }
    except Exception as e:
        logger.exception("An error occurred while processing the request")
        raise HTTPException(status_code=500, detail="Internal server error")
