import uvicorn

from fullstack_test.api_config import API_HOST, API_PORT

uvicorn.run(
    "fullstack_test.api_routes:app",
    host=API_HOST,
    port=API_PORT,
    workers=1
)