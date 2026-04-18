-- Run this SQL in your Supabase SQL Editor to create the table for the book analyses

CREATE TABLE IF NOT EXISTS public.book_analyses (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    ia_identifier TEXT NOT NULL UNIQUE,
    title TEXT NOT NULL,
    author TEXT,
    publication_year INTEGER,
    cover_image_url TEXT,
    one_liner_hook TEXT,
    why_it_matters TEXT,
    chapter_breakdowns JSONB DEFAULT '[]'::JSONB,
    best_ideas JSONB DEFAULT '[]'::JSONB,
    quotes JSONB DEFAULT '[]'::JSONB,
    criticism TEXT,
    verdict TEXT,
    actionable_takeaways JSONB DEFAULT '[]'::JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Enable RLS (Row Level Security) if not already done, you can uncomment this if you want restrictive access
-- ALTER TABLE public.book_analyses ENABLE ROW LEVEL SECURITY;

-- Allow public read access to book analyses
-- CREATE POLICY "Public can view analyses" ON public.book_analyses FOR SELECT USING (true);
