import ChefsBhojan from "./components/ChefsBhojan"
import MainPage from "./components/MAIN"
import MyComponent from "./components/MyComponent"
import { Routes, Route } from 'react-router-dom'

function App() {

  return (
    <>
      <Routes>
        <Route path="/" element={<MainPage />} />
        <Route path="/dhavali" element={<ChefsBhojan outlet={"Dhavali"} />} />
        <Route path="/ponda" element={<ChefsBhojan outlet={"Ponda"} />} />
        <Route path="/dhavalimenu" element={<MyComponent outlet={"Dhavali"} />} />
        <Route path="pondamenu" element={<MyComponent outlet={"Ponda"} />} />
      </Routes>
    </>
  )
}

export default App