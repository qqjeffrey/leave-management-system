from fastapi import APIRouter, Depends
from app.interfaces.schemas.user_schema import RegisterRequest, RegisterResponse
from app.use_cases.register_user import RegisterUserUseCase

router = APIRouter(prefix="/auth")

def get_register_user_use_case():
    return RegisterUserUseCase()

@router.post("/register", response_model=RegisterResponse)
def register_user(
    request: RegisterRequest,
    use_case: RegisterUserUseCase = Depends(get_register_user_use_case)
):
    user = use_case.execute(
        email=request.email,
        name=request.name,
        password=request.password
    )
    return RegisterResponse(
        email=user.email,
        name=user.name,
        message="Registration successful"
    )
