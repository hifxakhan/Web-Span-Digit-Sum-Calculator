# Web-Span-Digit-Sum-Calculator
This Python script extracts all the <span> elements from a given webpage and sums up all the numeric values found within them.

Features
1. Ignores SSL certificate errors for HTTPS websites.
2. Uses BeautifulSoup for HTML parsing.
3. Sums only numeric values inside <span> tags.

Requirements
1. Python 3.x
2. beautifulsoup4

You can install BeautifulSoup with: pip install beautifulsoup4

Usage
1. Clone the repository: git clone <your-repo-url>
2. Run the script: python span_sum_calculator.py
3. Enter the URL of the website you want to scrape when prompted.
4. The script will output the sum of all numeric values inside <span> tags.

Example
Enter URL: https://example.com
Total sum of digits in span tags: 125

Notes
The script only considers digits inside <span> elements, Non-numeric content inside <span> tags is ignored.
