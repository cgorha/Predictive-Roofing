import { createStore } from 'vuex';
import axios from 'axios';
import router from '../router';

const API_BASE_URL = 'http://127.0.0.1:8000/api/v1';

const store = createStore({
    state: {
        user: null,
        userToken: localStorage.getItem('userToken') || null,
        isAuthenticated: !!localStorage.getItem('userToken'),
        state: null,
    },
    mutations: {
        setUser(state, userData) {
            state.user = userData;
            state.isAuthenticated = true;
        },
        setUserToken(state, token) {
            state.userToken = token;
            localStorage.setItem('userToken', token);
            axios.defaults.headers.common["Authorization"] = "Token " + token;
            state.isAuthenticated = !!token;
        },
        clearUserState(state) {
            state.user = null;
            state.userToken = null;
            state.isAuthenticated = false;
            localStorage.removeItem('userToken');
            axios.defaults.headers.common["Authorization"] = "";
        }
    },
    actions: {
        async login({ commit, dispatch }, credentials) {
            try {
                const response = await axios.post(`${API_BASE_URL}/token/login/`, credentials);
                const token = response.data.auth_token;
                commit('setUserToken', token);
                await dispatch('fetchUser');
                router.push('/dashboard');
            } catch (error) {
                console.error("Error during login:", error);

            }
        },
        async logout({ commit }) {
            commit('clearUserState');
            router.push('/log-in');
        },
        async fetchUser({ commit, state }) {
            if (!state.userToken) return;

            try {
                const response = await axios.get(`${API_BASE_URL}/hi/`, {
                    headers: {
                        'Authorization': `Token ${state.userToken}`,
                    }
                });
                commit('setUser', response.data);
            } catch (error) {
                console.error("Error fetching user data:", error);
            }
        },
    }
});

export default store;
