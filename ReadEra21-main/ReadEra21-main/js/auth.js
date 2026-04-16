document.addEventListener("DOMContentLoaded", () => {

    const loginForm = document.getElementById("loginForm");

    if (loginForm) {
        loginForm.addEventListener("submit", async (e) => {
            e.preventDefault();

            const email = document.getElementById("loginEmail").value.trim();
            const password = document.getElementById("loginPassword").value.trim();

            try {
                const res = await AuthService.signIn(email, password);

                if (!res.success) {
                    alert(res.error);
                    return;
                }

                console.log("Login success ✅");

                // 🔥 FORCE REDIRECT
                setTimeout(() => {
                    window.location.href = "index.html";
                }, 500);

            } catch (err) {
                console.error(err);
                alert("Login failed");
            }
        });
    }

});