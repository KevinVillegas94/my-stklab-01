import axios from '../../lib/axios';

export const login = async (credentials) => {
  const response = await axios.post('auth/token/', credentials);
  return response.data;
};

export const refreshToken = async () => {
  const response = await axios.post('auth/token/refresh/');
  return response.data;
};

export const logout = async () => {
  await axios.post('auth/logout/');  // Backend debe invalidar el refresh token
};