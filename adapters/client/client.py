import httpx
import logging


logger = logging.getLogger('main_logger')


WORKER_URL = 'http://www.localhost:8001'


class WorkerClient:
    def __init__(self):
        self.url = WORKER_URL

    async def get_info(self):
        logger.debug("Poxy request to Worker client")
        try:
            async with httpx.AsyncClient() as client:
                return await client.get(self.url + '/getInfo')
        except Exception:
            return "Unable to stablish connection with Worker."
