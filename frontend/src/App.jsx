import ChefsBhojan from "./components/ChefsBhojan"
import MyComponent from "./components/MyComponent"
import { Routes, Route } from 'react-router-dom'

function App() {

  return (
    <>
      <Routes>
        <Route path="/" element={<ChefsBhojan />} />
        <Route path="/menu" element={<MyComponent />} />
      </Routes>
    </>
  )
}

export default App