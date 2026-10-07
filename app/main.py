from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.erreurs import PARAMETRE_INVALIDE, ErreurEntree
from app.routes import conversion, math, texte, validation

VERSION = "1.0.0"

app = FastAPI(title="Mini API", version=VERSION)

app.include_router(math.router)
app.include_router(texte.router)
app.include_router(conversion.router)
app.include_router(validation.router)


@app.exception_handler(ErreurEntree)
async def entree_invalide(request: Request, exc: ErreurEntree):
    return JSONResponse(status_code=400, content={"detail": str(exc)})


# FastAPI répond 422 par défaut, le sujet demande 400
@app.exception_handler(RequestValidationError)
async def type_invalide(request: Request, exc: RequestValidationError):
    return JSONResponse(status_code=400, content={"detail": PARAMETRE_INVALIDE})


@app.get("/sante")
def sante():
    return {"statut": "ok", "version": VERSION}
