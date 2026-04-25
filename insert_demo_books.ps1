$Headers = @{
    "apikey" = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJvam5tc2VyemNtaXVid2JkYnB3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzYzMTEwNTUsImV4cCI6MjA5MTg4NzA1NX0.GX7Lkr5l_qD1iSAKzKaAb82crlZJIPuBWm3ebfiqIho"
    "Authorization" = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJvam5tc2VyemNtaXVid2JkYnB3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzYzMTEwNTUsImV4cCI6MjA5MTg4NzA1NX0.GX7Lkr5l_qD1iSAKzKaAb82crlZJIPuBWm3ebfiqIho"
    "Content-Type" = "application/json"
    "Prefer" = "return=minimal"
}

$Body = '[
    {
        "ia_identifier": "meditations_george_long",
        "title": "Meditations",
        "author": "Marcus Aurelius",
        "publication_year": 161,
        "cover_image_url": "https://placehold.co/300x400/1e293b/fbbf24?text=Meditations",
        "one_liner_hook": "The most powerful man in the world wrote a private diary telling himself to stop complaining, be a better person, and remember he is going to die.",
        "why_it_matters": "He had absolute power over the Roman Empire but spent his nights in freezing military tents writing notes to himself about how to not be a terrible person.",
        "chapter_breakdowns": [{"chapter": "Book II: The Morning Prep", "key_idea": "People are going to suck today. Be ready for it.", "impact": "When you expect people to be flawed, you stop being chronically disappointed by them."}],
        "best_ideas": ["The Obstacle Is the Way", "Throw Away Your Interpretations"],
        "quotes": [{"quote": "You have power over your mind - not outside events.", "commentary": "The foundational thesis of Stoicism."}],
        "criticism": "Can border on emotional suppression.",
        "verdict": "A mandatory operating system update for your brain.",
        "actionable_takeaways": ["Take 2 minutes tomorrow morning to remind yourself you will deal with difficult people, and it will not dictate your mood."]
    },
    {
        "ia_identifier": "the-art-of-war-sun-tzu",
        "title": "The Art of War",
        "author": "Sun Tzu",
        "publication_year": 1910,
        "cover_image_url": "https://placehold.co/300x400/7f1d1d/fca5a5?text=Art+of+War",
        "one_liner_hook": "This 2,500-year-old military manual is secretly the best business, negotiation, and life strategy book ever written.",
        "why_it_matters": "In a world of startup pitch decks and office politics, The Art of War reads like a leaked playbook for winning without fighting.",
        "chapter_breakdowns": [{"chapter": "Attack by Stratagem", "key_idea": "The supreme excellence is to break the enemy resistance without fighting.", "impact": "This chapter invented win/win before it was cringe."}],
        "best_ideas": ["Win before you fight", "Invincibility is defense; vulnerability is opportunity"],
        "quotes": [{"quote": "If you know the enemy and know yourself, you need not fear the result of a hundred battles.", "commentary": "The quote demands homework before heroics."}],
        "criticism": "Amoral by design.",
        "verdict": "Read this if you make decisions under uncertainty.",
        "actionable_takeaways": ["Run a pre-mortem before your next big decision."]
    },
    {
        "ia_identifier": "the-prince-machiavelli-1532",
        "title": "The Prince",
        "author": "Niccolo Machiavelli",
        "publication_year": 1532,
        "cover_image_url": "https://placehold.co/300x400/064e3b/6ee7b7?text=The+Prince",
        "one_liner_hook": "The original handbook for ruthlessness that is so brutally honest, his name became a psychological disorder.",
        "why_it_matters": "We like to pretend the world runs on justice, but Machiavelli proved it runs on leverage and fear. It is the dark psychology manual that explains every corporate takeover.",
        "chapter_breakdowns": [{"chapter": "Chapter XVII", "key_idea": "It is better to be feared than loved, if you cannot be both.", "impact": "Machiavelli strips away the idealism of leadership."}],
        "best_ideas": ["The ends justify the means", "Appearances matter more than reality"],
        "quotes": [{"quote": "Men judge generally more by the eye than by the hand.", "commentary": "Perception is reality."}],
        "criticism": "Assumes people are inherently evil.",
        "verdict": "A fascinating look at power dynamics.",
        "actionable_takeaways": ["Protect your reputation above all else."]
    }
]'

Invoke-RestMethod -Uri "https://bojnmserzcmiubwbdbpw.supabase.co/rest/v1/book_analyses?on_conflict=ia_identifier" -Method Post -Headers $Headers -Body $Body
