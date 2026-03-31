from flask import Flask
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)

@app.route("/")
def test_chrome():
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Remote(
            command_executor="http://standalone-chrome:4444/wd/hub",
            options=chrome_options
        )

        driver.get("https://www.google.com")

        title = driver.title

        driver.quit()

        return f"✅ Chrome is working! Page title: {title}"

    except Exception as e:
        return f"❌ Error: {str(e)}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)