import os

ECAC_URL = os.getenv("ECAC_URL", "https://cav.receita.fazenda.gov.br/")
CHROME_USER_DATA_DIR = os.getenv("CHROME_USER_DATA_DIR", "")
AUTO_SELECT_CERT_JSON = os.getenv(
    "AUTO_SELECT_CERT_JSON",
    '[{"pattern":"https://cav.receita.fazenda.gov.br"}]'
)
PAGELOAD_TIMEOUT = int(os.getenv("PAGELOAD_TIMEOUT", "120"))
