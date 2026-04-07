from typing import Optional, List
from fastapi import APIRouter, Path, Body, HTTPException
from pydantic import BaseModel, Field, EmailStr, NonNegativeInt, PositiveFloat


router = APIRouter()


# ---------- Auth ----------
class LoginRequest(BaseModel):
	email: EmailStr = Field(..., example="user@example.com")
	password: str = Field(..., min_length=8, example="S3nh@F0rt3!")


class TokenResponse(BaseModel):
	access_token: str = Field(..., example="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...")
	token_type: str = Field("bearer", example="bearer")
	expires_in_seconds: NonNegativeInt = Field(900, example=900)


@router.post("/auth/login", response_model=TokenResponse, summary="Login (mock)")
async def login(payload: LoginRequest = Body(...)) -> TokenResponse:
	if payload.password == "invalid":
		raise HTTPException(status_code=401, detail="Invalid credentials")
	return TokenResponse(
		access_token="fake-jwt-token-123",
		token_type="bearer",
		expires_in_seconds=900,
	)


# ---------- Payments ----------
class ChargeRequest(BaseModel):
	amount: PositiveFloat = Field(..., example=149.90)
	currency: str = Field(..., example="BRL")
	description: Optional[str] = Field(None, example="Assinatura Premium")


class ChargeResponse(BaseModel):
	id: str = Field(..., example="ch_01HZX1ABCDXYZ")
	status: str = Field(..., example="approved")
	authorized_amount: PositiveFloat = Field(..., example=149.90)
	currency: str = Field(..., example="BRL")


@router.post("/payments/charge", response_model=ChargeResponse, summary="Criar cobrança (mock)")
async def create_charge(payload: ChargeRequest = Body(...)) -> ChargeResponse:
	return ChargeResponse(
		id="ch_fake_123",
		status="approved",
		authorized_amount=payload.amount,
		currency=payload.currency,
	)


# ---------- KYC ----------
class KycVerifyRequest(BaseModel):
	document_number: str = Field(..., example="12345678900")
	full_name: str = Field(..., example="João da Silva")
	email: EmailStr = Field(..., example="joao.silva@example.com")


class KycVerifyResponse(BaseModel):
	request_id: str = Field(..., example="kyc_req_abc123")
	status: str = Field(..., example="in_review")
	estimated_completion_seconds: NonNegativeInt = Field(120, example=120)


@router.post("/kyc/verify", response_model=KycVerifyResponse, summary="Iniciar verificação KYC (mock)")
async def kyc_verify(payload: KycVerifyRequest = Body(...)) -> KycVerifyResponse:
	return KycVerifyResponse(
		request_id="kyc_req_demo_001",
		status="in_review",
		estimated_completion_seconds=120,
	)


# ---------- Loans ----------
class LoanContract(BaseModel):
	contract_id: str = Field(..., example="loan_ctr_0001")
	customer_name: str = Field(..., example="Maria Souza")
	amount: PositiveFloat = Field(..., example=5000.00)
	installments: NonNegativeInt = Field(..., example=12)
	monthly_rate: float = Field(..., example=0.024)
	status: str = Field(..., example="active")


@router.get("/loans/contracts/{contract_id}", response_model=LoanContract, summary="Consultar contrato (mock)")
async def get_contract(
	contract_id: str = Path(..., example="loan_ctr_0001"),
) -> LoanContract:
	return LoanContract(
		contract_id=contract_id,
		customer_name="Maria Souza",
		amount=5000.00,
		installments=12,
		monthly_rate=0.024,
		status="active",
	)

