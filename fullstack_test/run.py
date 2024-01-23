import uvicorn

uvicorn.run(
    "fullstack_test.api_routes:app",
    host="0.0.0.0",
    port=8000,
    workers=1
)