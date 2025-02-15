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
      e.preventDefault()

      // Reset error messages
      document.querySelectorAll(".error-message").forEach((el) => el.remove())

      // Validate form
      let isValid = true
      const name = document.getElementById("name")
      const email = document.getElementById("email")
      const password = document.getElementById("password")
      const confirmPassword = document.getElementById("confirmPassword")

      if (name && name.value.trim() === "") {
        showError(name, "Name is required")
        isValid = false
      }

      if (email && email.value.trim() === "") {
        showError(email, "Email is required")
        isValid = false
      }

      if (password && password.value.length < 8) {
        showError(password, "Password must be at least 8 characters long")
        isValid = false
      }

      if (confirmPassword && password && confirmPassword.value !== password.value) {
        showError(confirmPassword, "Passwords do not match")
        isValid = false
      }

      if (isValid) {
        // Remove the preventDefault to allow form submission
        e.target.submit()
      }
    })
  }
})

function showError(input, message) {
  const errorElement = document.createElement("div")
  errorElement.className = "error-message text-red-500 text-sm mt-1"
  errorElement.textContent = message
  input.parentNode.insertBefore(errorElement, input.nextSibling)
}

