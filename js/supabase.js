const SUPABASE_URL = "https://bojnmserzcmiubwbdbpw.supabase.co";
const SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJvam5tc2VyemNtaXVid2JkYnB3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzYzMTEwNTUsImV4cCI6MjA5MTg4NzA1NX0.GX7Lkr5l_qD1iSAKzKaAb82crlZJIPuBWm3ebfiqIho";

let supabaseClient = null;
try {
    if (typeof supabase !== 'undefined') {
        supabaseClient = supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
    } else {
        console.error("Supabase library not loaded. Check your CDN script tag.");
    }
} catch (e) {
    console.error("Failed to initialize Supabase:", e);
}

// ================= AUTH =================
const AuthService = {
    async signUp(email, password, fullName) {
        if (!supabaseClient) return { success: false, error: "Supabase not initialized" };
        const { data, error } = await supabaseClient.auth.signUp({
            email,
            password,
            options: { data: { full_name: fullName } }
        });
        if (error) return { success: false, error: error.message };
        return { success: true, data };
    },

    async signIn(email, password) {
        if (!supabaseClient) return { success: false, error: "Supabase not initialized" };
        const { data, error } = await supabaseClient.auth.signInWithPassword({ email, password });
        if (error) return { success: false, error: error.message };
        setTimeout(() => {
            window.location.href = "index.html";
        }, 300);
        return { success: true, data };
    },

    async signOut() {
        if (supabaseClient) await supabaseClient.auth.signOut();
        window.location.href = "index.html";
    },

    async getUser() {
        if (!supabaseClient) return null;
        const { data } = await supabaseClient.auth.getUser();
        return data.user;
    },

    async isAuthenticated() {
        if (!supabaseClient) return false;
        const { data } = await supabaseClient.auth.getSession();
        return data.session !== null;
    }
};

// ================= BOOK =================
const BookService = {
    async getFeaturedBooks(limit = 8) {
        if (!supabaseClient) return { success: false, books: [] };
        const { data, error } = await supabaseClient
            .from('books')
            .select('*')
            .limit(limit);
        if (error) return { success: false, books: [] };
        return { success: true, books: data };
    },

    async getBookById(id) {
        if (!supabaseClient) return { success: false, book: null };
        const { data, error } = await supabaseClient
            .from('books')
            .select('*')
            .eq('id', id)
            .single();
        if (error) return { success: false, book: null };
        return { success: true, book: data };
    }
};

// ================= GLOBAL UI SYNC =================
const syncAuthUI = async () => {
    const user = await AuthService.getUser();
    const authLink = document.getElementById('auth-link');
    const logoutLink = document.getElementById('logout-link');
    const libraryLink = document.getElementById('library-link');
    const profileLink = document.getElementById('profile-link');

    if (user) {
        if (authLink) authLink.style.display = 'none';
        if (logoutLink) {
            logoutLink.style.display = 'inline-flex';
            logoutLink.onclick = (e) => {
                e.preventDefault();
                AuthService.signOut();
            };
        }
        if (libraryLink) libraryLink.style.display = 'block';
        if (profileLink) profileLink.style.display = 'block';
    } else {
        if (authLink) {
            authLink.style.display = 'inline-flex';
            authLink.href = 'auth.html';
        }
        if (logoutLink) logoutLink.style.display = 'none';
        if (libraryLink) libraryLink.style.display = 'none';
        if (profileLink) profileLink.style.display = 'none';
    }
};

document.addEventListener('DOMContentLoaded', syncAuthUI);
window.AuthService = AuthService;
window.BookService = BookService;
window.syncAuthUI = syncAuthUI;
window.supabaseClient = supabaseClient;