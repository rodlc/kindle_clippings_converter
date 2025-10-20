import os
import csv
import sys
from datetime import datetime
from bs4 import BeautifulSoup

def transform_highlights(input_folder, output_file):
    # Open the output CSV file for writing
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Book', 'Author', 'Location', 'Highlight', 'Conversion'])
        
        last_book_title = None  # Variable to track the change of books
        highlight_counter = 0   # Initialize highlight counter
        
        # Iterate over each HTML file in the input folder
        for filename in os.listdir(input_folder):
            if filename.endswith('.html'):
                input_file = os.path.join(input_folder, filename)
                
                # Read the HTML file
                with open(input_file, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                # Create a BeautifulSoup object to parse the HTML
                soup = BeautifulSoup(content, 'html.parser')
                
                # Find the book title and author
                book_title = soup.find('div', class_='bookTitle').text.strip()
                book_author = soup.find('div', class_='authors').text.strip()
                
                # Check if the book has changed
                if book_title != last_book_title:
                    highlight_counter = 0  # Reset highlight counter if it's a new book
                    last_book_title = book_title  # Update last_book_title to current
                
                # Get the current timestamp for the conversion date
                conversion_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                # Find all the chapter elements
                chapter_elements = soup.find_all('div', class_='sectionHeading')
                for chapter_index, chapter_element in enumerate(chapter_elements, start=1):
                    chapter_title = chapter_element.text.strip()
                    
                    # Find the highlight elements within the current chapter
                    highlight_elements = chapter_element.find_next_siblings('div', class_='noteText')
                    for highlight in highlight_elements:
                        # Check if the highlight belongs to the current chapter
                        if highlight.find_previous_sibling('div', class_='sectionHeading') != chapter_element:
                            break
                        highlight_counter += 1  # Increment highlight counter
                        
                        # Extract the highlight text
                        highlight_text = highlight.text.strip()
                        current_chapter = f"[Chapter {chapter_index}] {chapter_title} [{highlight_counter}]"
                        
                        # Write the highlight information to the CSV file
                        writer.writerow([book_title, book_author, current_chapter, highlight_text, conversion_date])

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_folder> <output_file>")
        sys.exit(1)
    input_folder = sys.argv[1]
    output_file = sys.argv[2]
    transform_highlights(input_folder, output_file)
