from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.config import ECAC_URL, CHROME_USER_DATA_DIR, AUTO_SELECT_CERT_JSON, PAGELOAD_TIMEOUT

def build_driver():
    opts = Options()
    if CHROME_USER_DATA_DIR:
        opts.add_argument(f"--user-data-dir={CHROME_USER_DATA_DIR}")
    if AUTO_SELECT_CERT_JSON:
        opts.add_argument(f'--auto-select-certificate-for-urls={AUTO_SELECT_CERT_JSON}')
    driver = webdriver.Chrome(options=opts)
    driver.set_page_load_timeout(PAGELOAD_TIMEOUT)
    return driver

def login_ecac(driver):
    driver.get(ECAC_URL)
    wait = WebDriverWait(driver, 60)
    try:
        btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(., 'Certificado') and contains(., 'digital')]")
        ))
        btn.click()
    except Exception:
        try:
            link = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(., 'Certificado') and contains(., 'digital')]")
            ))
            link.click()
        except Exception:
            pass
    wait.until(EC.presence_of_element_located(
        (By.XPATH, "//*[contains(., 'e-CAC')] | //*[contains(., 'Centro Virtual de Atendimento')]")
    ))
    return True

if __name__ == "__main__":
    d = build_driver()
    try:
        if login_ecac(d):
            print("✅ Login no eCAC concluído (provável).")
    finally:
        pass
