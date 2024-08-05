import React from "react"
import WelcomeMessage from "./WelcomeMessage"
import MenuButton from "./MenuButton"

function ChefsBhojan({ outlet }) {

  return (
    <main className="flex overflow-hidden flex-col items-center px-14 pt-56 pb-32 mx-auto w-full tracking-tight bg-yellow-400 max-w-[480px]">
      <img
        loading="lazy"
        src="/logo.png"
        alt="Chefs Bhojan logo"
        className="object-contain self-stretch w-full aspect-[1.2]"
      />
      <WelcomeMessage outlet={outlet} />
      <MenuButton outlet={outlet} />
    </main>
  )
}

export default ChefsBhojan
