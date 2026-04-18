# ============================================
# READERA - 50 HIGHLY DEMANDED EBOOKS GENERATOR
# Based on worldwide bestseller data
# ============================================

import json
import random
from datetime import datetime

# 50 highly demanded books (Genre-wise)
# Data from worldwide bestsellers, Goodreads, Amazon

books_data = [
    # FICTION
    {"title": "The Housemaid", "author": "Freida McFadden", "genre": "Fiction", "subgenre": "Thriller", "pages": 336, "summary": "A psychological thriller about a woman who takes a job as a housemaid in a wealthy family's home, only to discover dark secrets.", "cover_color": "#8B4513"},
    {"title": "Fourth Wing", "author": "Rebecca Yarros", "genre": "Fiction", "subgenre": "Fantasy", "pages": 528, "summary": "A dragon-riding fantasy novel set in a war college where riders compete to survive.", "cover_color": "#6B21A5"},
    {"title": "Iron Flame", "author": "Rebecca Yarros", "genre": "Fiction", "subgenre": "Fantasy", "pages": 640, "summary": "The sequel to Fourth Wing, continuing the epic fantasy adventure.", "cover_color": "#6B21A5"},
    {"title": "Lessons in Chemistry", "author": "Bonnie Garmus", "genre": "Fiction", "subgenre": "Historical", "pages": 400, "summary": "A brilliant scientist in the 1960s becomes a cooking show host, challenging societal norms.", "cover_color": "#0EA5E9"},
    {"title": "Tomorrow, and Tomorrow, and Tomorrow", "author": "Gabrielle Zevin", "genre": "Fiction", "subgenre": "Contemporary", "pages": 416, "summary": "A story of friendship, creativity, and success spanning decades in the world of video game design.", "cover_color": "#10B981"},
    
    # THRILLER
    {"title": "The Silent Patient", "author": "Alex Michaelides", "genre": "Thriller", "subgenre": "Psychological", "pages": 336, "summary": "A woman kills her husband and then stops speaking. A therapist tries to uncover why.", "cover_color": "#1E293B"},
    {"title": "The Girl on the Train", "author": "Paula Hawkins", "genre": "Thriller", "subgenre": "Psychological", "pages": 336, "summary": "A commuting woman becomes entangled in a missing persons investigation.", "cover_color": "#4B5563"},
    {"title": "Gone Girl", "author": "Gillian Flynn", "genre": "Thriller", "subgenre": "Psychological", "pages": 432, "summary": "A husband becomes the prime suspect in his wife's disappearance.", "cover_color": "#991B1B"},
    {"title": "The Guest List", "author": "Lucy Foley", "genre": "Thriller", "subgenre": "Mystery", "pages": 336, "summary": "A wedding on a remote island turns deadly.", "cover_color": "#047857"},
    {"title": "The Last Thing He Told Me", "author": "Laura Dave", "genre": "Thriller", "subgenre": "Mystery", "pages": 320, "summary": "A woman's husband disappears, leaving only a note saying 'Protect her'.", "cover_color": "#0EA5E9"},
    
    # ROMANCE
    {"title": "It Ends With Us", "author": "Colleen Hoover", "genre": "Romance", "subgenre": "Contemporary", "pages": 384, "summary": "A powerful story about love, resilience, and breaking cycles.", "cover_color": "#DB2777"},
    {"title": "It Starts With Us", "author": "Colleen Hoover", "genre": "Romance", "subgenre": "Contemporary", "pages": 336, "summary": "The sequel to It Ends With Us, continuing the emotional journey.", "cover_color": "#DB2777"},
    {"title": "Ugly Love", "author": "Colleen Hoover", "genre": "Romance", "subgenre": "Contemporary", "pages": 336, "summary": "A passionate and emotional romance about love and healing.", "cover_color": "#E11D48"},
    {"title": "Verity", "author": "Colleen Hoover", "genre": "Romance", "subgenre": "Romantic Suspense", "pages": 336, "summary": "A writer discovers a disturbing manuscript that blurs truth and fiction.", "cover_color": "#7E22CE"},
    {"title": "The Love Hypothesis", "author": "Ali Hazelwood", "genre": "Romance", "subgenre": "Romantic Comedy", "pages": 368, "summary": "A fake dating romance set in academia.", "cover_color": "#F97316"},
    
    # SCIENCE FICTION
    {"title": "Dune", "author": "Frank Herbert", "genre": "Science Fiction", "subgenre": "Epic", "pages": 896, "summary": "A classic epic of politics, religion, and ecology on the desert planet Arrakis.", "cover_color": "#D97706"},
    {"title": "Project Hail Mary", "author": "Andy Weir", "genre": "Science Fiction", "subgenre": "Adventure", "pages": 496, "summary": "An astronaut wakes up alone in space with no memory, trying to save humanity.", "cover_color": "#059669"},
    {"title": "The Martian", "author": "Andy Weir", "genre": "Science Fiction", "subgenre": "Adventure", "pages": 384, "summary": "An astronaut stranded on Mars uses science to survive.", "cover_color": "#DC2626"},
    {"title": "Children of Time", "author": "Adrian Tchaikovsky", "genre": "Science Fiction", "subgenre": "Space Opera", "pages": 624, "summary": "A civilization of evolved spiders challenges human survival.", "cover_color": "#65A30D"},
    {"title": "Foundation", "author": "Isaac Asimov", "genre": "Science Fiction", "subgenre": "Space Opera", "pages": 256, "summary": "The classic novel about a galactic empire and the science of psychohistory.", "cover_color": "#2563EB"},
    
    # FANTASY
    {"title": "A Court of Thorns and Roses", "author": "Sarah J. Maas", "genre": "Fantasy", "subgenre": "Romantasy", "pages": 448, "summary": "A mortal girl is drawn into a dangerous world of faeries.", "cover_color": "#7E22CE"},
    {"title": "A Court of Mist and Fury", "author": "Sarah J. Maas", "genre": "Fantasy", "subgenre": "Romantasy", "pages": 656, "summary": "The sequel continuing the epic faerie romance.", "cover_color": "#7E22CE"},
    {"title": "The Name of the Wind", "author": "Patrick Rothfuss", "genre": "Fantasy", "subgenre": "Epic", "pages": 672, "summary": "A legendary hero tells his life story to a chronicler.", "cover_color": "#B45309"},
    {"title": "The Way of Kings", "author": "Brandon Sanderson", "genre": "Fantasy", "subgenre": "Epic", "pages": 1008, "summary": "The first book in The Stormlight Archive epic fantasy series.", "cover_color": "#1D4ED8"},
    {"title": "Mistborn", "author": "Brandon Sanderson", "genre": "Fantasy", "subgenre": "Epic", "pages": 544, "summary": "A heist story set in a world where the Dark Lord has won.", "cover_color": "#B45309"},
    
    # MYSTERY
    {"title": "The Thursday Murder Club", "author": "Richard Osman", "genre": "Mystery", "subgenre": "Cozy", "pages": 384, "summary": "Four elderly friends in a retirement village solve cold cases.", "cover_color": "#059669"},
    {"title": "The Man Who Died Twice", "author": "Richard Osman", "genre": "Mystery", "subgenre": "Cozy", "pages": 384, "summary": "The second Thursday Murder Club mystery.", "cover_color": "#059669"},
    {"title": "The Bullet That Missed", "author": "Richard Osman", "genre": "Mystery", "subgenre": "Cozy", "pages": 368, "summary": "The third installment in the Thursday Murder Club series.", "cover_color": "#059669"},
    {"title": "The Last Devil to Die", "author": "Richard Osman", "genre": "Mystery", "subgenre": "Cozy", "pages": 368, "summary": "The fourth Thursday Murder Club mystery.", "cover_color": "#059669"},
    {"title": "The Maid", "author": "Nita Prose", "genre": "Mystery", "subgenre": "Cozy", "pages": 304, "summary": "A hotel maid finds a guest dead and becomes the prime suspect.", "cover_color": "#0891B2"},
    
    # SELF HELP
    {"title": "Atomic Habits", "author": "James Clear", "genre": "Self Help", "subgenre": "Productivity", "pages": 320, "summary": "A practical guide to building good habits and breaking bad ones.", "cover_color": "#EA580C"},
    {"title": "The Psychology of Money", "author": "Morgan Housel", "genre": "Self Help", "subgenre": "Finance", "pages": 256, "summary": "Timeless lessons on wealth, greed, and happiness.", "cover_color": "#0F766E"},
    {"title": "Thinking, Fast and Slow", "author": "Daniel Kahneman", "genre": "Self Help", "subgenre": "Psychology", "pages": 512, "summary": "How our two thinking systems shape our decisions.", "cover_color": "#475569"},
    {"title": "Deep Work", "author": "Cal Newport", "genre": "Self Help", "subgenre": "Productivity", "pages": 304, "summary": "Rules for focused success in a distracted world.", "cover_color": "#1E3A8A"},
    {"title": "The 7 Habits of Highly Effective People", "author": "Stephen R. Covey", "genre": "Self Help", "subgenre": "Leadership", "pages": 432, "summary": "A holistic approach to solving personal and professional problems.", "cover_color": "#854D0E"},
    
    # BUSINESS
    {"title": "Zero to One", "author": "Peter Thiel", "genre": "Business", "subgenre": "Entrepreneurship", "pages": 224, "summary": "Notes on startups and how to build the future.", "cover_color": "#0F172A"},
    {"title": "The Lean Startup", "author": "Eric Ries", "genre": "Business", "subgenre": "Entrepreneurship", "pages": 336, "summary": "How today's entrepreneurs use continuous innovation to create businesses.", "cover_color": "#166534"},
    {"title": "Good to Great", "author": "Jim Collins", "genre": "Business", "subgenre": "Management", "pages": 320, "summary": "Why some companies make the leap and others don't.", "cover_color": "#1E3A8A"},
    {"title": "Start With Why", "author": "Simon Sinek", "genre": "Business", "subgenre": "Leadership", "pages": 256, "summary": "How great leaders inspire action.", "cover_color": "#B45309"},
    {"title": "The Infinite Game", "author": "Simon Sinek", "genre": "Business", "subgenre": "Leadership", "pages": 272, "summary": "How great businesses achieve long-lasting success.", "cover_color": "#B45309"},
    
    # BIOGRAPHY
    {"title": "Steve Jobs", "author": "Walter Isaacson", "genre": "Biography", "subgenre": "Technology", "pages": 656, "summary": "The exclusive biography of Apple co-founder Steve Jobs.", "cover_color": "#1E293B"},
    {"title": "Elon Musk", "author": "Walter Isaacson", "genre": "Biography", "subgenre": "Technology", "pages": 688, "summary": "The biography of the world's most controversial entrepreneur.", "cover_color": "#1E293B"},
    {"title": "Becoming", "author": "Michelle Obama", "genre": "Biography", "subgenre": "Politics", "pages": 448, "summary": "The memoir of former First Lady Michelle Obama.", "cover_color": "#BE123C"},
    {"title": "The Diary of a Young Girl", "author": "Anne Frank", "genre": "Biography", "subgenre": "History", "pages": 288, "summary": "The famous diary of Anne Frank during WWII.", "cover_color": "#92400E"},
    {"title": "I Am Malala", "author": "Malala Yousafzai", "genre": "Biography", "subgenre": "Activism", "pages": 288, "summary": "The story of the youngest Nobel Peace Prize winner.", "cover_color": "#0F766E"},
    
    # HISTORY
    {"title": "Sapiens", "author": "Yuval Noah Harari", "genre": "History", "subgenre": "World History", "pages": 464, "summary": "A brief history of humankind.", "cover_color": "#1E3A8A"},
    {"title": "Homo Deus", "author": "Yuval Noah Harari", "genre": "History", "subgenre": "Future Studies", "pages": 464, "summary": "A brief history of tomorrow.", "cover_color": "#1E3A8A"},
    {"title": "The Silk Roads", "author": "Peter Frankopan", "genre": "History", "subgenre": "World History", "pages": 656, "summary": "A new history of the world focusing on the East.", "cover_color": "#854D0E"},
    {"title": "Guns, Germs, and Steel", "author": "Jared Diamond", "genre": "History", "subgenre": "Anthropology", "pages": 528, "summary": "The fates of human societies.", "cover_color": "#475569"},
    {"title": "The Wright Brothers", "author": "David McCullough", "genre": "History", "subgenre": "American History", "pages": 336, "summary": "The story of the invention of flight.", "cover_color": "#2563EB"}
]

# Generate Supabase insert SQL
print("="*60)
print("📚 GENERATING 50 EBOOKS DATA")
print("="*60)

# Create SQL insert statements
sql_statements = []
for book in books_data[:50]:
    # Create a summary with proper length
    summary = book['summary'][:500]
    
    sql = f"""INSERT INTO books (title, author, summary, genre, subcategory, total_pages, cover_url, pdf_url, views) VALUES (
    '{book['title'].replace("'", "''")}',
    '{book['author'].replace("'", "''")}',
    '{summary.replace("'", "''")}',
    '{book['genre']}',
    '{book['subgenre']}',
    {book['pages']},
    'https://placehold.co/300x400/{book['cover_color'].lstrip("#")}/white?text={book['title'].replace(" ", "+")[:20]}',
    'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf',
    0
);"""
    sql_statements.append(sql)

# Save to file
with open('books_data.sql', 'w', encoding='utf-8') as f:
    f.write("-- ReadEra - 50 Highly Demanded Books\n")
    f.write("-- Generated from worldwide bestseller data\n\n")
    for stmt in sql_statements:
        f.write(stmt + "\n\n")

print(f"✅ Generated {len(sql_statements)} SQL insert statements")
print("📁 Saved to: books_data.sql")

# Also save as JSON for reference
with open('books_data.json', 'w', encoding='utf-8') as f:
    json.dump(books_data[:50], f, ensure_ascii=False, indent=2)

print("✅ Saved to: books_data.json")

# Print summary by genre
genre_counts = {}
for book in books_data[:50]:
    genre = book['genre']
    genre_counts[genre] = genre_counts.get(genre, 0) + 1

print("\n📊 Books by Genre:")
for genre, count in genre_counts.items():
    print(f"   {genre}: {count} books")

print("\n" + "="*60)
print("🎉 Done! Now run this SQL in Supabase SQL Editor")
print("="*60)