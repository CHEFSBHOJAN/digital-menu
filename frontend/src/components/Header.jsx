import { useNavigate } from "react-router-dom"
import React from "react"

function Header({ outletName }) {
  const navigate = useNavigate()

  const home = () => {
    navigate('/')
  }
  return (
    <header className="flex gap-5 justify-between items-center text-xs text-center">
      <img
        loading="lazy"
        src="/logo.png"
        alt=""
        className="object-contain shrink-0 self-stretch aspect-[1.2] w-[60px]"
      />
      <div className="flex flex-col self-stretch my-auto">
        <div className="self-start text-black">You are at</div>
        <div className="font-bold text-red-900">{outletName}, Goa</div>
      </div>
      <button onClick={home}><img
        loading="lazy"
        src="https://cdn.builder.io/api/v1/image/assets/TEMP/d99c00fbe069e9fad227d82294749b04f863341faa217f167b366579b6250666?apiKey=eb2769a799454c22a06552d614e601b9&&apiKey=eb2769a799454c22a06552d614e601b9"
        alt=""
        className="object-contain shrink-0 self-stretch my-auto aspect-[1.29] w-[31px]"
      />
      </button>
    </header>
  )
}

export default Header
