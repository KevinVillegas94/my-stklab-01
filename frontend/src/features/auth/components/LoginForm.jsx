import { useAuth } from '../hooks/useAuth'

const LoginForm = () => {
    const { login, isLoading } = useAuth()

    const handleSubmit = (e) => {
        e.preventDefault()
        login({
            username: e.target.username.value,
            password: e.target.password.value
        })
    }

    return (
        <form onSubmit={handleSubmit}>
            {/* Tus campos de formulario */}
        </form>
    )
}