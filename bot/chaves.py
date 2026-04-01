# Arquivo que carregar e gerencia as variaveis de chaves de API que estão dentro do .env
 
import os
from dotenv import load_dotenv

load_dotenv()

CHAVE_API_TELEGRAM = os.getenv("TOKEN_TELEGRAM")
CHAVE_API_OPENROUTER = os.getenv("OPENROUTER_TOKEN")