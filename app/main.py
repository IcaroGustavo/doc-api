from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.routers.api_docs import router as api_docs_router
from app.routers.mock_apis import router as mock_apis_router


def create_app() -> FastAPI:
	app = FastAPI(
		title="FinFlow API Portal (White Label)",
		description="Portal centralizador de documentação de APIs - Exemplo White Label",
		version="1.0.0",
		docs_url="/docs",
		redoc_url="/redoc",
		openapi_url="/openapi.json",
	)

	# CORS básico para facilitar testes locais
	app.add_middleware(
		CORSMiddleware,
		allow_origins=["*"],
		allow_credentials=True,
		allow_methods=["*"],
		allow_headers=["*"],
	)

	# Arquivos estáticos
	app.mount("/static", StaticFiles(directory="app/static"), name="static")

	# Rotas
	app.include_router(api_docs_router)
	app.include_router(mock_apis_router, prefix="/mock", tags=["Mock APIs"])

	return app


app = create_app()


if __name__ == "__main__":
	import uvicorn

	uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

