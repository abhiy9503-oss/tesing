from flask import Flask
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

app = Flask(__name__)

@app.route("/")
def test():
    print("🔥 Route triggered → Starting Selenium")

    try:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        print("🚀 Connecting to Chrome...")

        driver = webdriver.Remote(
            command_executor="http://standalone-chrome:4444/wd/hub",
            options=options
        )

        print("🌐 Opening website...")
        driver.get("https://example.com")

        # Wait so you can SEE session in Selenium UI
        time.sleep(5)

        title = driver.title

        print("✅ Page loaded:", title)

        driver.quit()

        return f"""
        ✅ SELENIUM IS WORKING<br>
        🌐 Opened: example.com<br>
        📄 Title: {title}<br>
        🔥 Check Selenium UI → session should appear
        """

    except Exception as e:
        print("❌ ERROR:", e)
        return f"❌ Error: {str(e)}"

app.run(host="0.0.0.0", port=3000)
