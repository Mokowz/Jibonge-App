import { createApp } from 'vue';
import { createStore } from 'vuex';
import App from './App.vue'

const app = createApp({App}); 

const store = createStore({
  state() {
    return {
      loggedIn: false,
    };
  },

  mutations: { 
    setLoggedIn(state, value) {
      state.loggedIn = value;
    }
  }
});

export default store

app.use(store); // Use the Vuex store with the app

// console.log(store.state.loggedIn)

// export default app; // Export the app instance
