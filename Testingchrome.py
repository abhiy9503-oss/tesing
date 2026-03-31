from flask import Flask
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

app = Flask(__name__)

@app.route("/")
def test():
    print("🔥 Route triggered")

    options = Options()
    options.add_argument("--headless")

    driver = webdriver.Remote(
        command_executor="http://standalone-chrome:4444/wd/hub",
        options=options
    )

    driver.get("https://example.com")

    time.sleep(5)  # so you can SEE session

    title = driver.title

    driver.quit()

    return f"✅ Selenium working: {title}"

app.run(host="0.0.0.0", port=3000)
