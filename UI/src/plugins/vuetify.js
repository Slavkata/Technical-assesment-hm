
import Vue from 'vue'
import Vuetify from 'vuetify/lib'

Vue.use(Vuetify)

const vuetify = new Vuetify({
  theme: {
    themes: {
      light: {
        primary: '#051F4A;',
        secondary: '#1971FF',
        anchor: '#8c9eff',
        success: '#056903',
        error: '#780101'
      },
    },
  },
})

export default vuetify