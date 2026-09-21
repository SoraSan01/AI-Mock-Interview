import { Route, Routes } from 'react-router-dom'
import './App.css'
import Login from './pages/Login'
import PublicLayout from './layout/publicLayout'

function App() {
  return (
    <Routes>
      <Route element={<PublicLayout/>}>
         <Route path="/" element={<Login />} />
         <Route path="/feature" element={<Login />} />
         <Route path="/practice" element={<Login />} />
         <Route path="/login" element={<Login />} />
      </Route>
    </Routes>
  )
}

export default App