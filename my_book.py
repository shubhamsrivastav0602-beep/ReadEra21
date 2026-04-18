from book_generator import BookGenerator

# Create generator
gen = BookGenerator()

# Generate outline
outline = gen.generate_outline(
    title="The Psychology of Money",
    genre="Finance",
    target_audience="General readers interested in personal finance",
    chapters=10
)

print("Outline created!")

# Generate each chapter
for i, chapter in enumerate(outline.chapters, 1):
    content = gen.generate_chapter(chapter)
    print(f"Chapter {i}: {chapter.title}")
    
    # Save to file
    with open(f"chapter_{i}.txt", "w") as f:
        f.write(content)

print("Book generated successfully!")

# Export to EPUB
gen.export_to_epub("my_book.epub")
print("EPUB created!")