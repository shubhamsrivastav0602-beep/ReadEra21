# ============================================
# GENERATE BOOK COVERS (PUBLIC DOMAIN)
# ============================================

import json
import requests
from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

# Create covers folder
os.makedirs("covers", exist_ok=True)

# Public domain books data (50 books)
books = [
    {"title": "Pride and Prejudice", "author": "Jane Austen", "genre": "Romance", "color": "#8B4513"},
    {"title": "Frankenstein", "author": "Mary Shelley", "genre": "Horror", "color": "#1E293B"},
    {"title": "Dracula", "author": "Bram Stoker", "genre": "Horror", "color": "#991B1B"},
    {"title": "Sherlock Holmes", "author": "Arthur Conan Doyle", "genre": "Mystery", "color": "#0F766E"},
    {"title": "Great Expectations", "author": "Charles Dickens", "genre": "Fiction", "color": "#475569"},
    {"title": "Moby Dick", "author": "Herman Melville", "genre": "Adventure", "color": "#1E3A8A"},
    {"title": "Wuthering Heights", "author": "Emily Bronte", "genre": "Romance", "color": "#854D0E"},
    {"title": "Jane Eyre", "author": "Charlotte Bronte", "genre": "Romance", "color": "#BE123C"},
    {"title": "Crime and Punishment", "author": "Fyodor Dostoevsky", "genre": "Psychological", "color": "#0F172A"},
    {"title": "Anna Karenina", "author": "Leo Tolstoy", "genre": "Romance", "color": "#881337"},
    {"title": "Alice in Wonderland", "author": "Lewis Carroll", "genre": "Fantasy", "color": "#0D9488"},
    {"title": "The Picture of Dorian Gray", "author": "Oscar Wilde", "genre": "Gothic", "color": "#047857"},
    {"title": "The Time Machine", "author": "H.G. Wells", "genre": "Sci-Fi", "color": "#2563EB"},
    {"title": "Tom Sawyer", "author": "Mark Twain", "genre": "Children", "color": "#D97706"},
    {"title": "Huckleberry Finn", "author": "Mark Twain", "genre": "Children", "color": "#D97706"},
    {"title": "The Call of the Wild", "author": "Jack London", "genre": "Adventure", "color": "#B45309"},
    {"title": "Little Women", "author": "Louisa May Alcott", "genre": "Fiction", "color": "#C2410C"},
    {"title": "Treasure Island", "author": "Robert Louis Stevenson", "genre": "Adventure", "color": "#0F766E"},
    {"title": "The Odyssey", "author": "Homer", "genre": "Epic", "color": "#6D28D9"},
    {"title": "The Iliad", "author": "Homer", "genre": "Epic", "color": "#6D28D9"},
    {"title": "The Scarlet Letter", "author": "Nathaniel Hawthorne", "genre": "Romance", "color": "#DC2626"},
    {"title": "Heart of Darkness", "author": "Joseph Conrad", "genre": "Psychological", "color": "#0F172A"},
    {"title": "The Secret Garden", "author": "Frances Burnett", "genre": "Children", "color": "#059669"},
    {"title": "Peter Pan", "author": "J.M. Barrie", "genre": "Children", "color": "#0891B2"},
    {"title": "The Wizard of Oz", "author": "L. Frank Baum", "genre": "Fantasy", "color": "#E11D48"},
    {"title": "The Count of Monte Cristo", "author": "Alexandre Dumas", "genre": "Adventure", "color": "#7E22CE"},
    {"title": "The Three Musketeers", "author": "Alexandre Dumas", "genre": "Adventure", "color": "#7E22CE"},
    {"title": "Les Misérables", "author": "Victor Hugo", "genre": "Historical", "color": "#1E3A8A"},
    {"title": "Dr Jekyll and Mr Hyde", "author": "Robert Louis Stevenson", "genre": "Gothic", "color": "#334155"},
    {"title": "Around the World in 80 Days", "author": "Jules Verne", "genre": "Adventure", "color": "#0D9488"},
    {"title": "20,000 Leagues Under the Sea", "author": "Jules Verne", "genre": "Sci-Fi", "color": "#0D9488"},
]

def create_cover(title, author, color, index):
    """Create a book cover image"""
    # Create image
    img = Image.new('RGB', (300, 400), color=color)
    draw = ImageDraw.Draw(img)
    
    # Try to load font, fallback to default
    try:
        font_title = ImageFont.truetype("arial.ttf", 24)
        font_author = ImageFont.truetype("arial.ttf", 16)
    except:
        font_title = ImageFont.load_default()
        font_author = ImageFont.load_default()
    
    # Wrap title text
    wrapped_title = textwrap.wrap(title, width=15)
    
    # Calculate position (center)
    y = 150
    for line in wrapped_title:
        bbox = draw.textbbox((0, 0), line, font=font_title)
        w = bbox[2] - bbox[0]
        draw.text(((300 - w) // 2, y), line, fill='white', font=font_title)
        y += 35
    
    # Draw author
    y += 20
    author_text = f"by {author}"
    bbox = draw.textbbox((0, 0), author_text, font=font_author)
    w = bbox[2] - bbox[0]
    draw.text(((300 - w) // 2, y), author_text, fill='#e2e8f0', font=font_author)
    
    # Draw genre at bottom
    genre_text = f"📚 {books[index]['genre'] if index < len(books) else 'Classic'}"
    bbox = draw.textbbox((0, 0), genre_text, font=font_author)
    w = bbox[2] - bbox[0]
    draw.text(((300 - w) // 2, 360), genre_text, fill='#cbd5e1', font=font_author)
    
    # Save
    filename = f"covers/{title.replace(' ', '_').replace('/', '_')}.jpg"
    img.save(filename)
    return filename

print("🎨 Generating book covers...")
for i, book in enumerate(books[:30]):
    filename = create_cover(book['title'], book['author'], book['color'], i)
    print(f"✅ Created: {filename}")

print(f"\n✅ Generated {len(books[:30])} covers in 'covers/' folder")