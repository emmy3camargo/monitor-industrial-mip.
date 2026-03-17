import time
import random
import json

# Simulação de limites de segurança (Padrão Porto Itapoá)
LIMITES = {
    "temperatura_max": 85.0,
    "vibracao_critica": 0.05,
    "status_sensor": "ATIVO"
}

def ler_sensor_industrial():
    # Simulando dados reais de um RTG (Guindaste)
    dados = {
        "timestamp": time.strftime("%H:%M:%S"),
        "temp": round(random.uniform(20.0, 90.0), 2),
        "vibracao": round(random.uniform(0.01, 0.08), 3)
    }
    return dados

def analisar_seguranca(leitura):
    # Lógica de intertravamento (Interlock)
    if leitura["temp"] > LIMITES["temperatura_max"]:
        return "⚠️ ALERTA: Superaquecimento! Parada de Emergência."
    if leitura["vibracao"] > LIMITES["vibracao_critica"]:
        return "🛑 ERRO: Vibração excessiva detectada."
    return "✅ Operação Normal"

# Loop Principal de Monitoramento
print("--- Iniciando Monitor de Processos (MIP) ---")
try:
    while True:
        dados_atuais = ler_sensor_industrial()
        status = analisar_seguranca(dados_atuais)
        
        print(f"[{dados_atuais['timestamp']}] Temp: {dados_atuais['temp']}°C | {status}")
        
        time.sleep(2) # Intervalo de 2 segundos entre leituras
except KeyboardInterrupt:
    print("\nMonitoramento encerrado pelo usuário.")
