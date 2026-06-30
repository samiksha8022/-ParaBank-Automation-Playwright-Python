import pytest
import os
import base64
from pytest_html import extras

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    report.extras = getattr(report, "extras", [])

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            os.makedirs("reports/screenshots", exist_ok=True)
            screenshot_path = f"reports/screenshots/{item.name}.png"

            try:
                page.screenshot(path=screenshot_path)

                # Base64 mein convert karo
                with open(screenshot_path, "rb") as f:
                    image_data = base64.b64encode(f.read()).decode("utf-8")

                report.extras.append(
                    extras.image(image_data, mime_type="image/png")
                )
            except Exception as e:
                print(f"Screenshot nahi le saka: {e}")