import requests
from bs4 import BeautifulSoup
import csv
import os

# URL to scrape
URL = 'https://www.futbol24.com/team/Croatia/Dinamo-Zagreb/results/'
RESULTS_FILE = 'results.csv'

# Fetch the webpage
def fetch_results():
    response = requests.get(URL)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data: {response.status_code}")
    return response.text

# Parse match results
def parse_results(html):
    soup = BeautifulSoup(html, 'html.parser')
    results = []
    
    # Adjust selector based on actual webpage structure
    for match in soup.select('.match-row'): 
        date = match.select_one('.date').text.strip()
        teams = match.select_one('.teams').text.strip()
        score = match.select_one('.score').text.strip()
        
        results.append({
            'date': date,
            'teams': teams,
            'score': score
        })
    
    return results

# Load existing results or create a new CSV file if it doesn't exist
def load_existing_results():
    if not os.path.exists(RESULTS_FILE):
        with open(RESULTS_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['date', 'teams', 'score'])
        return []
    with open(RESULTS_FILE, 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)

# Save results to CSV file
def save_results(new_results):
    with open(RESULTS_FILE, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['date', 'teams', 'score'])
        for result in new_results:
            writer.writerow(result)

# Main function
def main():
    html = fetch_results()
    new_results = parse_results(html)
    existing_results = load_existing_results()
    
    # Filter only new results
    existing_dates = {result['date'] for result in existing_results}
    unique_results = [result for result in new_results if result['date'] not in existing_dates]
    
    if unique_results:
        save_results(unique_results)
        print(f"Added {len(unique_results)} new results.")
    else:
        print("No new results found.")

if __name__ == '__main__':
    main()
