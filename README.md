# Amazon Website Automation Testing Using Playwright and Pytest

## 1. Project Overview

This project automates the product search functionality on Amazon India using **Python, Playwright, and Pytest**.

The objective is to practice browser automation, validate search results, open product details, and generate an HTML test execution report.

The automation workflow is based on browser actions recorded using Playwright Codegen and adapted into a Pytest test function.

## 2. Project Objectives

- Automate the Amazon India website using Playwright.
- Search for wireless headphones under ₹2,000.
- Verify that product search results are displayed.
- Open the first product and verify that it belongs to Amazon India.
- Execute automated tests using Pytest.
- Generate an HTML report containing test execution results.
- Practice Git and GitHub commands for version control.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Playwright | Browser automation |
| Pytest | Test execution and test discovery |
| pytest-playwright | Playwright integration with Pytest |
| pytest-html | HTML test report generation |
| Chromium | Browser used for automation |
| Git | Version control |
| GitHub | Remote repository hosting |
| VS Code | Development environment |

## 4. Project Structure

```text
Amazon_Automation/
│
├── tests/
│   ├── test_amazon_search.py
│   └── test_amazon_product.py
│
├── .venv/
├── .gitignore
├── pytest.ini
├── requirements.txt
├── README.md
└── report.html
```

**File descriptions:**

- `tests/test_amazon_search.py` — contains the automated Amazon product search test.
- `tests/test_amazon_product.py` — reserved for future product-detail tests.
- `.venv/` — contains the project's Python virtual environment.
- `.gitignore` — excludes generated files and local environment files from Git.
- `pytest.ini` — contains Pytest discovery settings.
- `requirements.txt` — lists the Python packages required by the project.
- `README.md` — documents the project and its execution steps.
- `report.html` — generated HTML test report; this file is created when tests are executed.

## 5. Step-by-Step Implementation

### Step 1: Create the project folder

Created the project folder named `Amazon_Automation` and opened it in VS Code.

Opened the integrated terminal and navigated to the project directory:

```powershell
cd "C:\Users\LENOVO\OneDrive\Desktop\Amazon_Automation"
```

### Step 2: Create a virtual environment

Created an isolated Python environment for the project:

```powershell
python -m venv .venv
```

Activated the environment in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

The `(.venv)` prefix in the terminal indicates that the virtual environment is active.

### Step 3: Install the required packages

Installed Playwright, Pytest, the Pytest integration, and the HTML report plugin:

```powershell
python -m pip install pytest pytest-playwright pytest-html
```

Installed the Chromium browser required by Playwright:

```powershell
python -m playwright install chromium
```

### Step 4: Record browser actions using Playwright Codegen

Used Playwright Codegen to record browser interactions on Amazon India.

Executed:

```powershell
python -m playwright codegen https://www.amazon.in/
```

Codegen opened a browser window and recorded actions performed manually, including:

1. Opening Amazon India.
2. Clicking the search box.
3. Entering `wireless headphones under 2000`.
4. Submitting the search.

Codegen generated Python code containing Playwright locators and browser actions.

### Step 5: Adapt the generated code for Pytest

The initial Codegen output was a standalone Playwright script using a `run()` function and `sync_playwright()`.

To execute it through Pytest, the relevant browser actions were adapted into a function whose name begins with `test_`.

For example:

```python
def test_amazon_search(page: Page):
    ...
```

The `page` fixture is provided by the Playwright Pytest plugin. It manages the browser page for the test.

The standalone browser-launching and closing code was removed because the fixture manages the browser lifecycle.

The test was also adapted to verify the search results and open the first product. The original promotional-text click, Add to Cart action, and Buy Now action were excluded because they were unnecessary for validating product search, and Buy Now could initiate a real purchase.

### Step 6: Implement the automated test

The test performs the following operations:

1. Navigates to Amazon India.
2. Locates the search box using its accessible role and name.
3. Enters the search query.
4. Submits the search.
5. Locates the product search results.
6. Verifies that the first result is visible.
7. Opens the first product in a new tab.
8. Verifies that the new tab's URL belongs to Amazon India.

The test uses Playwright assertions through `expect()`.

Example assertion:

```python
expect(products.first).to_be_visible(timeout=20000)
```

This checks that the first search result becomes visible within the specified timeout.

### Step 7: Run the test with a visible browser

Executed the test using:

```powershell
python -m pytest tests/test_amazon_search.py -v -s --headed --slowmo 700
```

Command options:

- `-v` — displays detailed test results.
- `-s` — displays print statements in the terminal.
- `--headed` — opens a visible browser window.
- `--slowmo 700` — slows browser operations to make them easier to observe.

### Step 8: Generate the HTML report

Executed the following command:

```powershell
python -m pytest tests/test_amazon_search.py -v -s --headed --slowmo 700 --html=report.html --self-contained-html
```

The test executes in a visible browser, and the `pytest-html` plugin generates the report.

Command options:

- `--html=report.html` — saves the report to `report.html`.
- `--self-contained-html` — creates a self-contained HTML report.

To open the generated report in the default browser:

```powershell
start report.html
```

The report contains test execution information, including the test name and its pass/fail status.

## 6. How Pytest Discovers Tests

Pytest discovers test functions whose names start with `test_`, provided they are in files matching its configured discovery rules.

Example:

```python
def test_amazon_search(page: Page):
    ...
```

A standalone Codegen script does not automatically become a Pytest test just because it contains Playwright actions. It must be adapted to Pytest's test-discovery conventions.


## 7. Expected Result

When the test passes:

- Amazon India opens in Chromium.
- The search query is submitted.
- Product search results are displayed.
- The first product opens in a new tab.
- Assertions validate the expected behavior.
- Pytest records the test result.
- An HTML report is generated.


## 8. Conclusion

This project demonstrates a beginner-level website automation workflow using Playwright and Pytest. It covers browser interaction, test assertions, visible browser execution, HTML report generation, and version control using Git and GitHub.