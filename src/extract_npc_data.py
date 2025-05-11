import requests
from bs4 import BeautifulSoup
import os

def fetch_character_page(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch page: {url}")
        return None
    return BeautifulSoup(response.text, 'html.parser')

def extract_quotes(soup, max_quotes=10):
    quotes = []
    for li in soup.select("li"):
        text = li.get_text().strip()
        if 8 < len(text) < 200 and '"' in text:
            quotes.append(text.replace("\n", " "))
        if len(quotes) >= max_quotes:
            break
    return quotes

def save_npc_file(name, bio, quotes):
    os.makedirs("npc_data", exist_ok=True)
    path = os.path.join("npc_data", f"{name.lower().replace(' ', '_')}.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write("## BIO\n")
        f.write(bio.strip() + "\n\n")
        f.write("## QUOTES\n")
        for q in quotes:
            f.write(f"{q}\n")
    print(f"✅ Saved {name} to {path}")

# --- Manual BIO Input ---
character_name = "Tom_Riddle"
manual_bio = """
Through his own nature, Lord Voldemort was the ultimate epitome of pure evil, a man who constantly craved horror,
contention and bloodshed, and spread nothing but darkness and suffering anywhere he went, considered by many to be
'the most evil wizard in hundreds and hundreds of years'. His malevolence far exceeded that of any common evildoer 
and Dumbledore stated that he 'went beyond normal evil' in the extent of his crimes. Hagrid claimed that while all 
Dark wizards 'go bad', Voldemort went 'worse than worse'. Indeed, Voldemort speedily developed into a power-obsessed 
megalomaniac of the worst kind and the worst of any known Dark wizard, being considered by all to be far more evil than 
even Gellert Grindelwald. He was unable and unwilling to express remorse or empathy for the countless crimes he had 
committed. This was a stark contrast to Grindelwald, a well-meaning extremist who proved to display genuine remorse 
for his crimes and even before his fall, pity for those abused for their magic and even if only a little, care for his
followers, all which Voldemort completely lacked. These misanthropic traits were seen in his childhood, from stealing 
to disturbing incidences with other orphans. Dumbledore stated that the young Riddle had a certain disregard for rules. 
In his adult life, he performed the darkest forms of magic and valued no living thing other than himself. First and 
foremost, he loved causing a trail of never-ending death and destruction to justify his own nihilism. Hence, he was a 
prolific killer, as seen by his killing so many that he created an army of Inferi.
"""

# --- Fetch quotes ---
url = "https://harrypotter.fandom.com/wiki/Tom_Riddle"
soup = fetch_character_page(url)
if soup:
    quotes = extract_quotes(soup)
    save_npc_file(character_name, manual_bio, quotes)
