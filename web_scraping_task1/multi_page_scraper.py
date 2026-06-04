import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

# Create folder for all datasets
if not os.path.exists('scraped_data'):
    os.makedirs('scraped_data')

# List of Wikipedia pages to scrape (title, URL, description)
websites = [
    {
        'name': 'highest_grossing_films',
        'title': 'Highest Grossing Films',
        'url': 'https://en.wikipedia.org/wiki/List_of_highest-grossing_films'
    },
    {
        'name': 'most_populated_countries',
        'title': 'Most Populated Countries',
        'url': 'https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)'
    },
    {
        'name': 'largest_cities',
        'title': 'Largest Cities',
        'url': 'https://en.wikipedia.org/wiki/List_of_largest_cities'
    },
    {
        'name': 'olympic_medals',
        'title': 'Olympic Medal Count',
        'url': 'https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table'
    },
    {
        'name': 'tallest_buildings',
        'title': 'Tallest Buildings',
        'url': 'https://en.wikipedia.org/wiki/List_of_tallest_buildings'
    }
]

# Headers to avoid being blocked
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def scrape_wikipedia_table(url, page_name):
    """
    Scrape the first wikitable from a Wikipedia page
    """
    print(f"\n{'='*60}")
    print(f"📥 Scraping: {page_name}")
    print(f"{'='*60}")
    
    try:
        # Fetch the page
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code != 200:
            print(f"❌ Failed to fetch {page_name} (Status: {response.status_code})")
            return None
        
        print(f"✅ Connected successfully!")
        
        # Parse HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all wikitable tables
        tables = soup.find_all('table', class_='wikitable')
        
        if not tables:
            print(f"⚠️ No wikitable found on {page_name}")
            return None
        
        # Use the first table
        table = tables[0]
        
        # Extract headers
        headers_list = []
        header_row = table.find('tr')
        if header_row:
            for th in header_row.find_all('th'):
                header_text = th.get_text(strip=True)[:50]  # Limit length
                headers_list.append(header_text)
        
        # Extract data rows
        data = []
        rows = table.find_all('tr')[1:]  # Skip header row
        
        for row in rows:
            cols = row.find_all('td')
            if cols and len(cols) > 1:  # Ensure at least 2 columns
                row_data = []
                for col in cols[:len(headers_list)]:
                    # Clean the text
                    text = col.get_text(strip=True)
                    # Remove footnote numbers like [1], [2]
                    text = text.split('[')[0]
                    # Remove extra whitespace
                    text = ' '.join(text.split())
                    row_data.append(text)
                
                if row_data:
                    data.append(row_data)
        
        if not data:
            print(f"⚠️ No data rows found on {page_name}")
            return None
        
        # Create DataFrame
        df = pd.DataFrame(data, columns=headers_list[:len(data[0])])
        
        # Save to CSV
        filename = f"scraped_data/{page_name}.csv"
        df.to_csv(filename, index=False)
        
        print(f"✅ SCRAPED: {len(data)} rows × {len(df.columns)} columns")
        print(f"💾 Saved to: {filename}")
        
        return df
        
    except Exception as e:
        print(f"❌ Error scraping {page_name}: {str(e)}")
        return None

# Main scraping process
print("="*60)
print("🚀 STARTING MULTI-PAGE WEB SCRAPER")
print("="*60)
print(f"\n📋 Will scrape {len(websites)} different Wikipedia pages")
print("⏱️  Adding 2 second delay between requests to be respectful\n")

# Store all scraped data
all_datasets = {}
success_count = 0

# Scrape each website
for i, site in enumerate(websites, 1):
    print(f"\n[{i}/{len(websites)}] Processing...")
    
    df = scrape_wikipedia_table(site['url'], site['name'])
    
    if df is not None:
        all_datasets[site['name']] = df
        success_count += 1
    
    # Wait between requests to be polite to the server
    if i < len(websites):
        print("⏳ Waiting 2 seconds before next request...")
        time.sleep(2)

# Summary report
print("\n" + "="*60)
print("📊 SCRAPING COMPLETED!")
print("="*60)
print(f"✅ Successfully scraped: {success_count}/{len(websites)} pages")
print(f"📁 All files saved in 'scraped_data/' folder")

print("\n📋 FILES CREATED:")
for site in websites:
    filename = f"scraped_data/{site['name']}.csv"
    if os.path.exists(filename):
        size = os.path.getsize(filename)
        print(f"   ✓ {site['name']}.csv ({size:,} bytes)")
    else:
        print(f"   ✗ {site['name']}.csv (failed)")

# Show quick preview of first dataset
if all_datasets:
    print("\n🔍 PREVIEW OF FIRST DATASET:")
    first_name = list(all_datasets.keys())[0]
    print(f"\n📊 {first_name.upper()}:")
    print(all_datasets[first_name].head())