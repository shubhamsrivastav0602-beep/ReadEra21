import os
from supabase import create_client, Client

SUPABASE_URL = "https://ryzbikpzxphrsdctvqp.supabase.co"
SUPABASE_KEY = "sb_publishable_MPqGLh4Z15HdLuTRQ81SzA_Ssm9n"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

demo_books = [
    {
        "ia_identifier": "meditations_george_long",
        "title": "Meditations",
        "author": "Marcus Aurelius",
        "publication_year": 161,
        "cover_image_url": "https://placehold.co/300x400/1e293b/fbbf24?text=Meditations",
        "one_liner_hook": "The most powerful man in the world wrote a private diary telling himself to stop complaining, be a better person, and remember he's going to die.",
        "why_it_matters": "He had absolute power over the Roman Empire but spent his nights in freezing military tents writing notes to himself about how to not be a terrible person. It's the ultimate reality check for modern life.",
        "chapter_breakdowns": [
            {"chapter": "Book II: The Morning Prep", "key_idea": "People are going to suck today. Be ready for it.", "impact": "When you expect people to be flawed, you stop being chronically disappointed by them."}
        ],
        "best_ideas": ["The Obstacle Is the Way", "Throw Away Your Interpretations"],
        "quotes": [{"quote": "You have power over your mind - not outside events.", "commentary": "The foundational thesis of Stoicism."}]
    },
    {
        "ia_identifier": "the-art-of-war-sun-tzu",
        "title": "The Art of War",
        "author": "Sun Tzu",
        "publication_year": -500,
         "cover_image_url": "https://placehold.co/300x400/7f1d1d/fca5a5?text=Art+of+War",
        "one_liner_hook": "This 2,500-year-old military manual is secretly the best business, negotiation, and life strategy book ever written.",
        "why_it_matters": "In a world of startup pitch decks and office politics, The Art of War reads like a leaked playbook for winning without fighting.",
        "chapter_breakdowns": [
            {"chapter": "Attack by Stratagem", "key_idea": "The supreme excellence is to break the enemy's resistance without fighting.", "impact": "This chapter invented win/win before it was cringe."}
        ],
        "best_ideas": ["Win before you fight", "Invincibility is defense; vulnerability is opportunity"],
        "quotes": [{"quote": "If you know the enemy and know yourself, you need not fear the result of a hundred battles.", "commentary": "The quote demands homework before heroics."}]
    },
    {
        "ia_identifier": "the-prince-machiavelli-1532",
        "title": "The Prince",
        "author": "Niccolò Machiavelli",
        "publication_year": 1532,
        "cover_image_url": "https://placehold.co/300x400/064e3b/6ee7b7?text=The+Prince",
        "one_liner_hook": "The original handbook for ruthlessness that is so brutally honest, his name became a psychological disorder.",
        "why_it_matters": "We like to pretend the world runs on justice, but Machiavelli proved it runs on leverage and fear. It is the dark psychology manual that explains every corporate takeover.",
        "chapter_breakdowns": [
            {"chapter": "Chapter XVII", "key_idea": "It is better to be feared than loved, if you cannot be both.", "impact": "Machiavelli strips away the idealism of leadership."}
        ],
        "best_ideas": ["The ends justify the means", "Appearances matter more than reality"],
        "quotes": [{"quote": "Men judge generally more by the eye than by the hand.", "commentary": "Perception is reality."}]
    }
]

for book in demo_books:
    try:
        supabase.table("book_analyses").upsert(book, on_conflict="ia_identifier").execute()
        print(f"Inserted: {book['title']}")
    except Exception as e:
        print(f"Error inserting {book['title']}: {e}")
