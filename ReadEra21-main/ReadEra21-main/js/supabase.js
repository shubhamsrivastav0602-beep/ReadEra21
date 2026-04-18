const SUPABASE_URL = "https://bojnmserzcmiubwbdbpw.supabase.co";
const SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJvam5tc2VyemNtaXVid2JkYnB3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzYzMTEwNTUsImV4cCI6MjA5MTg4NzA1NX0.GX7Lkr5l_qD1iSAKzKaAb82crlZJIPuBWm3ebfiqIho";

const supabaseClient = supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);

// ================= AUTH =================
const AuthService = {

    async signUp(email, password, fullName) {
        const { data, error } = await supabaseClient.auth.signUp({
            email,
            password,
            options: { data: { full_name: fullName } }
        });
        if (error) return { success: false, error: error.message };
        return { success: true, data };
    },

    async signIn(email, password) {
        const { data, error } = await supabaseClient.auth.signInWithPassword({ email, password });
        if (error) return { success: false, error: error.message };

        // Wait briefly for session to be written, then redirect
        setTimeout(() => {
            window.location.href = "index.html";
        }, 300);

        return { success: true, data };
    },

    async signOut() {
        await supabaseClient.auth.signOut();
        window.location.href = "index.html";
    },

    async getUser() {
        const { data } = await supabaseClient.auth.getUser();
        return data.user;
    },

    // ✅ FIXED: async check using getSession() — reliable on all pages
    async isAuthenticated() {
        const { data } = await supabaseClient.auth.getSession();
        return data.session !== null;
    }
};

// ================= BOOK =================
const BookService = {

    async getFeaturedBooks(limit = 8) {
        const { data, error } = await supabaseClient
            .from('books')
            .select('*')
            .limit(limit);

        if (error) return { success: false, books: [] };
        return { success: true, books: data };
    },

    async getBookById(id) {
        const { data, error } = await supabaseClient
            .from('books')
            .select('*')
            .eq('id', id)
            .single();

        if (error) return { success: false, book: null };
        return { success: true, book: data };
    }
};