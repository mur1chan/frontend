/** @type {import('tailwindcss').Config} */
module.exports = {
  daisyui: {
    themes: ["light", "dark", "autumn", "nord"],
  },
  content: [
    "./templates/**/*.{html,js}",
    "./templates/**/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [require('daisyui'),],
}

