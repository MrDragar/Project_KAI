import json
import logging

from dotenv import dotenv_values


config = dotenv_values(".env")

API_TOKEN = config["API_TOKEN"]
ADMINS_ID = json.loads(config["ADMINS_ID"])

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
