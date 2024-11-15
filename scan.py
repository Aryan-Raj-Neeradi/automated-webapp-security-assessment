import sys
import time
from zapv2 import ZAPv2

# Set up the ZAP instance
target_url = sys.argv[1] if len(sys.argv) > 1 else 'https://targetwebsite.com'

# ZAP API Key (if required, change accordingly)
api_key = 'your_zap_api_key'
zap = ZAPv2(apikey=api_key)

# Start the scan
print(f'Starting ZAP scan on {target_url}')
zap.urlopen(target_url)

# Start Active Scan
print('Starting active scan...')
scan_id = zap.ascan.scan(target_url)
while int(zap.ascan.status(scan_id)) < 100:
    print(f'Scan progress: {zap.ascan.status(scan_id)}%')
    time.sleep(5)

# Fetch and save the report
print('Scan complete. Saving the report...')
html_report = zap.core.htmlreport()
with open('results/report.html', 'w') as report_file:
    report_file.write(html_report)

print(f'Report saved to results/report.html')

