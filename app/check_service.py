from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from axe_selenium_python import Axe
import time

def check_accessibility(url: str):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Chạy trong chế độ headless
    chrome_options.add_argument("--no-sandbox")  # Bỏ qua sandbox
    chrome_options.add_argument("--disable-dev-shm-usage")  # Giảm sử dụng bộ nhớ chia sẻ
    chrome_options.add_argument("--disable-gpu")  # Vô hiệu hóa GPU
    chrome_options.add_argument("--window-size=1920x1080")  # Đặt kích thước cửa sổ

    # Sử dụng ChromeDriver tương thích với Chrome
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get(url)
        time.sleep(5)  # Chờ để trang tải xong

        axe = Axe(driver)
        axe.inject()  # Chèn Axe vào trang
        results = axe.run()  # Chạy kiểm tra

        return {
            "url": url,
            "violations": results.get("violations", []),
            "passes": results.get("passes", []),
            "inapplicable": results.get("inapplicable", []),
            "incomplete": results.get("incomplete", [])
        }
    finally:
        driver.quit()  # Đảm bảo đóng driver
