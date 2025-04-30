import axios from 'axios';

const instance = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1/',
  withCredentials: true,  // Para cookies HTTPOnly
});

// Interceptor para errores globales
instance.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      window.location.href = '/login';  // Redirigir si no autenticado
    }
    return Promise.reject(error);
  }
);

export default instance;