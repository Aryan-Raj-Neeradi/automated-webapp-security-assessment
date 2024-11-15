# Automated Web Application Security Assessment

This project automates the security testing of web applications against the **OWASP Top 10** vulnerabilities using **OWASP ZAP**.

## Prerequisites

1. Python 3.x installed
2. OWASP ZAP installed
3. Basic knowledge of web application security

## Installation

Follow these steps to set up the project:

### Step 1: Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/your-username/automated-webapp-security-assessment.git
cd automated-webapp-security-assessment
```
## Step 2: Install Dependencies
Install the required Python packages:
```
pip install -r requirements.txt
```

## Step 3: Install OWASP ZAP

Download and install OWASP ZAP from the official site: OWASP ZAP Download

You can run OWASP ZAP in headless mode (no GUI) for automation:
```
zap.sh -daemon
```
## Step 4: Run the Security Scan

Run the scan.py script to start the automated web application security scan:

python scan.py --url https://targetwebsite.com

## Step 5: View the Report

After the scan completes, the results will be saved in the results/report.html 
file. Open it in a browser to view the detailed security findings.

## Continuous Integration

You can integrate this project into your CI/CD pipeline using GitHub Actions. The security scan will run automatically on every push to the repository.

## CI/CD Setup

GitHub Actions will automatically run the scan on every push to the repository:

1. Go to the .github/workflows/security-scan.yml file.
2. Customize the workflow as needed for your repository.

## About OWASP Top 10

The OWASP Top 10 is a list of the 10 most critical web application security risks. This project helps identify vulnerabilities such as:

Injection (SQL Injection, etc.)

Broken Authentication

Sensitive Data Exposure

XML External Entities (XXE)

Broken Access Control

Security Misconfiguration

Cross-Site Scripting (XSS)

Insecure Deserialization

Using Components with Known Vulnerabilities

Insufficient Logging & Monitoring

## You can install these dependencies using:
```
pip install -r requirements.txt
```
## scan.py (Main Python Script)
   
This Python script will run the OWASP ZAP scan and save the results in an HTML file.

##  .github/workflows/security-scan.yml (GitHub Actions for CI/CD)

This file sets up GitHub Actions to automatically run the security scan on every push to the repository.

##  Running the Project
   
## To run the project manually:

1. Clone the repository.
2. Install dependencies.
3. Run OWASP ZAP in daemon mode.
4. Run the scan.py script.
5. View the generated report in results/report.html.

## For CI/CD integration:

Push to your GitHub repository and GitHub Actions will automatically trigger the security scan.
