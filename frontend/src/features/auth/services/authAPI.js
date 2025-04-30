import axios from '../../../api/axios'

export const login = (credentials) => {
    return axios.post('auth/token/', credentials)
}

export const refreshToken = (refresh) => {
    return axios.post('auth/token/refresh/', { refresh })
}