from playwright.sync_api import sync_playwright

def test_saucedemo():

    with sync_playwright() as p:

        # Launch browser
        browser = p.chromium.launch(headless=False)

        # Open new page
        page = browser.new_page()

        # Navigate to SauceDemo
        page.goto("https://www.saucedemo.com/")

        # -------------------------
        # Login
        # -------------------------
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")

        page.click("#login-button")

        # Verify login
        if "inventory" in page.url:
            print("Login Successful!")

        # -------------------------
        # Add Product To Cart
        # -------------------------
        page.click("#add-to-cart-sauce-labs-backpack")

        print("Product added to cart successfully!")

        # Open cart
        page.click(".shopping_cart_link")

        # -------------------------
        # Checkout Flow
        # -------------------------
        page.click("#checkout")

        page.fill("#first-name", "John")
        page.fill("#last-name", "Doe")
        page.fill("#postal-code", "400001")

        page.click("#continue")

        # Finish checkout
        page.click("#finish")

        # Verify order completion
        success_message = page.locator(".complete-header").text_content()

        if success_message == "Thank you for your order!":
            print("Checkout completed successfully!")

        # Wait before closing browser
        page.wait_for_timeout(3000)

        browser.close()

# Run test
test_saucedemo()