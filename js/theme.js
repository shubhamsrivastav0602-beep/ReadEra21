// ============================================
// READERA - DARK MODE THEME MANAGER
// Anti-FOUC: apply dark immediately
(function(){
    try {
        var t = localStorage.getItem('readera_theme') || localStorage.getItem('theme');
        var sys = window.matchMedia('(prefers-color-scheme: dark)').matches;
        if (t === 'dark' || (!t && sys)) {
            document.documentElement.classList.add('dark-mode-pending');
            document.addEventListener('DOMContentLoaded', function() {
                document.body.classList.add('dark-mode', 'dark');
                document.documentElement.classList.remove('dark-mode-pending');
            });
        }
    } catch(e) {}
})();
// ============================================

const ThemeManager = {
    // Keys for localStorage
    STORAGE_KEY: 'readera_theme',

    // Theme values
    THEMES: {
        LIGHT: 'light',
        DARK: 'dark'
    },

    // Possible button IDs (handling inconsistencies in the codebase)
    BUTTON_IDS: ['theme-toggle', 'themeToggle', 'themeBtn'],

    // Initialize theme on page load
    init() {
        // Get saved theme or system preference
        const savedTheme = this.getSavedTheme();
        const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

        // Determine initial theme
        let initialTheme = savedTheme;
        if (!initialTheme) {
            initialTheme = systemPrefersDark ? this.THEMES.DARK : this.THEMES.LIGHT;
        }

        // Apply theme
        this.applyTheme(initialTheme);

        // Setup theme toggle button
        this.setupToggleButton();

        // Listen for system theme changes (optional)
        this.listenToSystemTheme();
    },

    // Get saved theme from localStorage
    getSavedTheme() {
        // Support both old 'theme' key and new 'readera_theme' key
        return localStorage.getItem(this.STORAGE_KEY) || localStorage.getItem('theme');
    },

    // Save theme to localStorage
    saveTheme(theme) {
        localStorage.setItem(this.STORAGE_KEY, theme);
        localStorage.setItem('theme', theme); // Backwards compatibility
    },

    // Apply theme to body
    applyTheme(theme) {
        if (theme === this.THEMES.DARK) {
            document.body.classList.add('dark-mode');
            document.body.classList.add('dark'); // Backwards compatibility
            this.updateToggleButtonIcon(true);
        } else {
            document.body.classList.remove('dark-mode');
            document.body.classList.remove('dark'); // Backwards compatibility
            this.updateToggleButtonIcon(false);
        }

        // Save to localStorage
        this.saveTheme(theme);

        // Dispatch event for other components to listen
        window.dispatchEvent(new CustomEvent('themeChanged', { detail: { theme: theme } }));
    },

    // Toggle between light and dark
    toggleTheme() {
        const isDarkMode = document.body.classList.contains('dark-mode') || document.body.classList.contains('dark');

        if (isDarkMode) {
            this.applyTheme(this.THEMES.LIGHT);
            this.showToast('Light mode activated', 'info');
        } else {
            this.applyTheme(this.THEMES.DARK);
            this.showToast('Dark mode activated', 'info');
        }
    },

    // Update toggle button icon based on current theme
    updateToggleButtonIcon(isDark) {
        this.BUTTON_IDS.forEach(id => {
            const toggleBtn = document.getElementById(id);
            if (!toggleBtn) return;

            if (isDark) {
                toggleBtn.innerHTML = '☀️';
                toggleBtn.setAttribute('aria-label', 'Switch to light mode');
            } else {
                toggleBtn.innerHTML = '🌙';
                toggleBtn.setAttribute('aria-label', 'Switch to dark mode');
            }
        });
    },

    // Setup theme toggle button event listener
    setupToggleButton() {
        let found = false;
        this.BUTTON_IDS.forEach(id => {
            const toggleBtn = document.getElementById(id);
            if (toggleBtn) {
                found = true;
                // Add listener directly instead of cloning to keep other potential listeners
                // but we use a named function to avoid duplicates
                toggleBtn.onclick = (e) => {
                    e.preventDefault();
                    this.toggleTheme();
                };

                // Update icon based on current state
                const isDark = document.body.classList.contains('dark-mode') || document.body.classList.contains('dark');
                this.updateToggleButtonIcon(isDark);
            }
        });

        if (!found) {
            console.warn('Theme toggle button not found! Check your button IDs.');
        }
    },

    // Listen to system theme changes (optional feature)
    listenToSystemTheme() {
        const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');

        // Only listen if user hasn't manually set a preference
        mediaQuery.addEventListener('change', (e) => {
            const savedTheme = this.getSavedTheme();

            // If user never manually chose a theme, follow system
            if (!savedTheme) {
                const newTheme = e.matches ? this.THEMES.DARK : this.THEMES.LIGHT;
                this.applyTheme(newTheme);
            }
        });
    },

    // Show toast notification
    showToast(message, type = 'info') {
        // Simple built-in toast if not defined elsewhere
        if (window.showToast && typeof window.showToast === 'function' && !window.showToast.isThemeToast) {
            window.showToast(message);
            return;
        }

        // Check if toast container exists
        let toastContainer = document.getElementById('theme-toast-container');
        if (!toastContainer) {
            toastContainer = document.createElement('div');
            toastContainer.id = 'theme-toast-container';
            toastContainer.style.cssText = `
                position: fixed;
                bottom: 20px;
                right: 20px;
                z-index: 10000;
                pointer-events: none;
            `;
            document.body.appendChild(toastContainer);
        }

        const toast = document.createElement('div');
        const colors = {
            success: '#10b981',
            error: '#ef4444',
            warning: '#f59e0b',
            info: '#3b82f6'
        };

        toast.style.cssText = `
            background: ${colors[type] || colors.info};
            color: white;
            padding: 12px 20px;
            margin-top: 10px;
            border-radius: 8px;
            font-size: 14px;
            font-weight: 500;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
            animation: themeSlideIn 0.3s ease;
            pointer-events: auto;
            cursor: pointer;
        `;

        toast.textContent = message;
        toastContainer.appendChild(toast);

        // Auto remove
        setTimeout(() => {
            toast.style.opacity = '0';
            toast.style.transition = 'opacity 0.3s ease';
            setTimeout(() => toast.remove(), 300);
        }, 2500);

        toast.onclick = () => toast.remove();
    },

    // Preload theme immediately
    preloadTheme() {
        const savedTheme = this.getSavedTheme();
        const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

        if (savedTheme === this.THEMES.DARK || (!savedTheme && systemPrefersDark)) {
            document.body.classList.add('dark-mode');
            document.body.classList.add('dark');
        }
    },

    // Setup mobile menu
    setupMobileMenu() {
        const menuBtn = document.getElementById('mobile-menu-btn');
        const navDrawer = document.getElementById('nav-drawer');
        if (menuBtn && navDrawer) {
            menuBtn.addEventListener('click', () => {
                const isOpen = navDrawer.classList.toggle('is-open');
                menuBtn.setAttribute('aria-expanded', isOpen);
                const icon = menuBtn.querySelector('i');
                if (icon) {
                    icon.classList.toggle('fa-bars', !isOpen);
                    icon.classList.toggle('fa-times', isOpen);
                }
            });

            // Close menu when clicking outside
            document.addEventListener('click', (e) => {
                if (navDrawer.classList.contains('is-open') && 
                    !navDrawer.contains(e.target) && 
                    !menuBtn.contains(e.target)) {
                    navDrawer.classList.remove('is-open');
                    menuBtn.setAttribute('aria-expanded', 'false');
                    const icon = menuBtn.querySelector('i');
                    if (icon) {
                        icon.classList.add('fa-bars');
                        icon.classList.remove('fa-times');
                    }
                }
            });
        }
    }
};

// Add CSS animations for toast
if (!document.getElementById('theme-toast-styles')) {
    const style = document.createElement('style');
    style.id = 'theme-toast-styles';
    style.textContent = `
        @keyframes themeSlideIn {
            from { transform: translateX(100%); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }
    `;
    document.head.appendChild(style);
}

// Preload theme immediately
ThemeManager.preloadTheme();

// Initialize theme when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    ThemeManager.init();
    ThemeManager.setupMobileMenu();
});

// Make ThemeManager globally available
window.ThemeManager = ThemeManager;
window.showToast = window.showToast || ThemeManager.showToast;
window.showToast.isThemeToast = true;