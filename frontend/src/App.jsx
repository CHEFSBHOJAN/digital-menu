import ChefsBhojan from "./components/ChefsBhojan"
import MainPage from "./components/MAIN"
import MyComponent from "./components/MyComponent"
import { Routes, Route } from 'react-router-dom'

function App() {

  return (
    <>
      <Routes>
        <Route path="/" element={<MainPage />} />
        <Route path="/margao" element={<ChefsBhojan outlet={"Margao"} />} />
        <Route path="/ponda" element={<ChefsBhojan outlet={"Ponda"} />} />
        <Route path="/margaomenu" element={<MyComponent outlet={"Margao"} />} />
        <Route path="pondamenu" element={<MyComponent outlet={"Ponda"} />} />
      </Routes>
    </>
  )
}

export default App