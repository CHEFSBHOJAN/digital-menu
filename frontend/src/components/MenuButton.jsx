import { useNavigate } from "react-router-dom"
import React from "react"

function MenuButton({ outlet }) {

  const navigate = useNavigate()

  const GotoMenu = () => {
    if (outlet === "Dhavali") {
      navigate('/dhavalimenu')
    }
    if (outlet === "Ponda") {
      navigate('/pondamenu')
    }
  }

  return (
    <button onClick={GotoMenu} className="flex gap-2 px-10 py-5 mt-14 text-sm font-bold text-white bg-red-900 rounded-3xl shadow-[0px_1px_5px_rgba(0,0,0,0.25)]">
      <span className="grow">Checkout Our Menu</span>
      <img
        loading="lazy"
        src="https://cdn.builder.io/api/v1/image/assets/TEMP/558da563c52a43c35ff3be4c9b7a12c9c45f041380d6c49d0d92dbc5f637c2e3?apiKey=eb2769a799454c22a06552d614e601b9&&apiKey=eb2769a799454c22a06552d614e601b9"
        alt=""
        className="object-contain shrink-0 my-auto w-2 aspect-[0.57]"
      />
    </button>
  )
}

export default MenuButton
