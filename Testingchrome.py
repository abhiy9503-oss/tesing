from flask import Flask
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

app = Flask(__name__)

@app.route("/")
def test():
    print("🔥 STEP 1: Route triggered")

    try:
        options = Options()
        options.add_argument("--headless")

        print("🚀 STEP 2: Connecting to Chrome")

        driver = webdriver.Remote(
            command_executor="http://standalone-chrome:4444/wd/hub",
            options=options
        )

        print("🌐 STEP 3: Opening website")

        driver.get("https://example.com")

        time.sleep(5)  # so you can see session

        title = driver.title

        print("✅ STEP 4: Page title fetched:", title)

        driver.quit()

        return f"""
        ✅ SCRIPT IS RUNNING<br>
        🚀 Selenium Connected<br>
        🌐 Opened example.com<br>
        📄 Title: {title}
        """

    except Exception as e:
        print("❌ ERROR:", e)
        return f"❌ Error: {str(e)}"

app.run(host="0.0.0.0", port=3000)
