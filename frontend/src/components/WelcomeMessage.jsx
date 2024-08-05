import React from "react"

function WelcomeMessage({ outlet }) {
  return (
    <section className="mt-36 text-lg text-center text-black">
      Welcome to Chefs Bhojan <br />
      <span className="font-bold text-red-900">{outlet}, Goa</span>
    </section>
  )
}

export default WelcomeMessage
