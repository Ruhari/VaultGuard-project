function togglePasswordVisibility(inputId, iconId) {
  const passwordInput = document.getElementById(inputId)
  const eyeIcon = document.getElementById(iconId)

  if (passwordInput.type === "password") {
    passwordInput.type = "text"
    eyeIcon.innerHTML = `
            <path d="M17.94 17.94a10 10 0 0 1-11.88 0"></path>
            <path d="M1 1l22 22"></path>
        `
  } else {
    passwordInput.type = "password"
    eyeIcon.innerHTML = `
            <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
            <circle cx="12" cy="12" r="3"></circle>
        `
  }
}

document.addEventListener("DOMContentLoaded", () => {
  const signupForm = document.querySelector("form")
  if (signupForm) {
    signupForm.addEventListener("submit", (e) => {
      // Form will be submitted to the server for validation
      console.log("Form submitted")
    })
  }
})

