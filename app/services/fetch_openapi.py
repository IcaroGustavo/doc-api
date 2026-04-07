import asyncio
from typing import List, Dict, Any
from pydantic import BaseModel, Field


class ApiSchemaMeta(BaseModel):
	title: str = Field(..., description="Título da API")
	version: str = Field(..., description="Versão da API")
	description: str = Field(..., description="Descrição breve da API")
	paths: Dict[str, Dict[str, Any]] = Field(default_factory=dict, description="Mapa de endpoints da API")

	def to_openapi_like(self) -> Dict[str, Any]:
		return {
			"openapi": "3.0.3",
			"info": {
				"title": self.title,
				"version": self.version,
				"description": self.description,
			},
			"paths": self.paths,
		}


async def _simulate_service_latency(min_ms: int = 30, max_ms: int = 120) -> None:
	delay = (min_ms + max_ms) / 2000.0  # valor simples e determinístico ~0.075s
	await asyncio.sleep(delay)


async def _fetch_auth_openapi() -> Dict[str, Any]:
	await _simulate_service_latency()
	model = ApiSchemaMeta(
		title="Auth Service",
		version="1.2.0",
		description="Gerencia autenticação, autorização e emissão de tokens.",
		paths={
			"/auth/login": {"post": {"summary": "Realiza login com credenciais"}},
			"/auth/refresh": {"post": {"summary": "Renova o token de acesso"}},
			"/auth/health": {"get": {"summary": "Verifica saúde do serviço"}},
		},
	)
	return model.to_openapi_like()


async def _fetch_payments_openapi() -> Dict[str, Any]:
	await _simulate_service_latency()
	model = ApiSchemaMeta(
		title="Payments Service",
		version="2.0.1",
		description="Processa pagamentos, estornos e conciliações.",
		paths={
			"/payments/charge": {"post": {"summary": "Cria uma cobrança"}},
			"/payments/refund": {"post": {"summary": "Realiza estorno"}},
			"/payments/health": {"get": {"summary": "Verifica saúde do serviço"}},
		},
	)
	return model.to_openapi_like()


async def _fetch_kyc_openapi() -> Dict[str, Any]:
	await _simulate_service_latency()
	model = ApiSchemaMeta(
		title="KYC Service",
		version="0.9.5",
		description="Executa verificações de identidade e compliance (KYC).",
		paths={
			"/kyc/verify": {"post": {"summary": "Inicia verificação de identidade"}},
			"/kyc/status/{id}": {"get": {"summary": "Consulta status da verificação"}},
			"/kyc/health": {"get": {"summary": "Verifica saúde do serviço"}},
		},
	)
	return model.to_openapi_like()


async def _fetch_loans_openapi() -> Dict[str, Any]:
	await _simulate_service_latency()
	model = ApiSchemaMeta(
		title="Loans Service",
		version="3.3.0",
		description="Orquestra propostas, contratos e parcelas de empréstimos.",
		paths={
			"/loans/proposals": {"post": {"summary": "Cria proposta de empréstimo"}},
			"/loans/contracts/{id}": {"get": {"summary": "Obtém contrato"}},
			"/loans/health": {"get": {"summary": "Verifica saúde do serviço"}},
		},
	)
	return model.to_openapi_like()


async def fetch_openapi_schemas() -> List[Dict[str, Any]]:
	"""
	Simula a busca assíncrona de 4 schemas OpenAPI de microsserviços.
	Retorna dicionários no formato OpenAPI-like com metadados e paths.
	"""
	results = await asyncio.gather(
		_fetch_auth_openapi(),
		_fetch_payments_openapi(),
		_fetch_kyc_openapi(),
		_fetch_loans_openapi(),
	)
	return list(results)

