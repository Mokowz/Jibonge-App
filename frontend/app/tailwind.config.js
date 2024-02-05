/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    screens: {
      sm: '480px',
      md: '768px',
      lg: '976px',
      xl: '1440px',
    },
    fontFamily: {
      'noto': ['Noto Sans', 'sans-serif'],
      'riot': ['Protest Riot', 'sans-serif'],
    },
    extend: {
      colors: {
        'darkBlue': 'rgb(23 23 23)',
      },
    },
  },
  plugins: [],
}

