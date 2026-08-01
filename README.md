# Ecommerce Automation Framework

## Project Overview

This is a Playwright + Pytest automation framework developed using the Page Object Model (POM) design pattern.

The framework automates the complete purchase flow of the SauceDemo application.

---

## Technologies Used

- Python
- Playwright
- Pytest
- Pytest-HTML
- Logging
- Page Object Model (POM)

---

## Project Structure

Ecommerce_Automation/

pages/
tests/
utilities/
reports/
logs/
conftest.py
pytest.ini
requirements.txt
README.md

---

## Test Scenarios

### Login Test

- Login with valid credentials
- Verify Inventory Page

---

### Product Test

- Select Backpack Product
- Add Product to Cart

---

### Cart Test

- Verify Product in Cart

---

### Checkout Test

- Enter Customer Details
- Complete Checkout
- Verify Order Success
- Logout

---

## Features

- Page Object Model
- Smoke Test Suite
- Regression Test Suite
- HTML Reports
- Screenshot on Failure
- Logging
- Reusable Framework

---

## Execute All Tests

```bash
pytest
```

## Execute Smoke Tests

```bash
pytest -m smoke --headed
```

## Execute Regression Tests

```bash
pytest -m regression --headed
```

## Generate HTML Report

```bash
pytest --html=reports/report.html --self-contained-html
```

---

## Author

Krishnaveni
Automation Test Engineer
Python | Playwright | Pytest