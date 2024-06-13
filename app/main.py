import os

import uvicorn
from fastapi import FastAPI

from app.routes.deck import router as deck_router
from app.routes.image import router as image_router

app = FastAPI()

app.include_router(deck_router, prefix="/decks")
app.include_router(image_router, prefix="/images")

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
