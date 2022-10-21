from fastapi import FastAPI
import logging
from adapters.client.client import WorkerClient

# Initialize logger
logger = logging.getLogger('main_logger')

# Create app
app = FastAPI()


@app.on_event("startup")
async def startup_event():
    logger.info('Starting application')


@app.on_event("shutdown")
async def startup_event():
    logger.info('Shutting down application')


@app.get("/getInfo")
async def get_info():
    logger.info('Received call to /getInfo endpoint')
    client = WorkerClient()
    return await client.get_info()
