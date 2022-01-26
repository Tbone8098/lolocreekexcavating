module.exports = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'lolo': {
          'green': '#639438'
        }
      },
      fontFamily: {
          'libre': ['Libre Baskerville'],
          'cinzel': ['Cinzel'],
          'bree': ['Bree Serif']
      }
    },
  },
  plugins: [],
}
