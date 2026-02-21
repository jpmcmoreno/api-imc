from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/")
def home():
    return {"mensaje": "API Pública de IMC. Usa /imc?peso=KG&altura=METROS"}

@app.get("/imc")
def calcular_imc(
    peso: float = Query(..., description="Peso en kilogramos"), 
    altura: float = Query(..., description="Altura en metros")
):
    if altura <= 0:
        return {"error": "La altura debe ser mayor a 0"}
    
    # Fórmula: Peso / Altura al cuadrado
    imc = peso / (altura ** 2)
    imc_resultado = round(imc, 2)
    
    # Clasificación rápida
    if imc_resultado < 18.5:
        estado = "Bajo peso"
    elif 18.5 <= imc_resultado < 25:
        estado = "Peso normal"
    elif 25 <= imc_resultado < 30:
        estado = "Sobrepeso"
    else:
        estado = "Obesidad"

    return {
        "imc": imc_resultado,
        "clasificacion": estado,
        "url_llamada": f"Calculado para {peso}kg y {altura}m"
    }
