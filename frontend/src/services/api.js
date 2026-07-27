import axios from "axios";

const api = axios.create({
    baseURL: "http://127.0.0.1:8000"
});

// Add JWT automatically
api.interceptors.request.use((config) => {

    const token = localStorage.getItem("token");

    if (token) {
        config.headers.Authorization = `Bearer ${token}`;
    }

    return config;
});

export default api;

// -----------------------------

export const createSession = async (title) => {

    const response = await api.post("/chat/session", {
        title
    });

    return response.data;
};

export const sendMessage = async (sessionId, prompt) => {

    const response = await api.post("/chat/send", {
        session_id: sessionId,
        prompt
    });

    return response.data;
};

export const getHistory = async (sessionId) => {

    const response = await api.get(
        `/history/${sessionId}`
    );

    return response.data;
};