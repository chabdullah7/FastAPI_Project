from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from app.api import routes_auth, routes_predict
from app.middleware.logging_middleware import LoggingMiddleware
from app.core.exceptions import register_exception_handler

print("Starting FastAPI app...")  

app = FastAPI(title='Car Price Prediction API')

print("Adding middleware...")      
# Link Middleware
app.add_middleware(LoggingMiddleware)

print("Including routers...")  
# Link Endpoints
app.include_router(routes_auth.router, tags=['Auth'])
app.include_router(routes_predict.router, tags=['Prediction'])

print("Setting up Prometheus metrics...")  
# Monitoring Using Prometheus
Instrumentator().instrument(app).expose(app)

print("Registering exception handlers...")  
# Add Exception Handler
register_exception_handler(app)

print("FastAPI app setup complete!") 