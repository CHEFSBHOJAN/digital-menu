import React from "react"
import VegIcon from '../assets/Veg_symbol.svg'
import NonVegIcon from '../assets/Non_veg_symbol.svg'

function MenuSection({ title, items, itemRefs }) {
  return (
    <section className="w-full flex flex-col flex-1 self-start">
      <h3 className="text-lg font-medium text-red-900">{title}</h3>
      <div className="flex flex-col gap-5 mt-2.5 text-xs leading-4 text-black">
        {items.map((item) => (
          <div key={item.id} ref={(el) => { if (el) itemRefs.current[item.id] = el; }} className="flex justify-between items-center w-full">
            <div className="relative flex items-center mr-2 w-full">
              <div className="dish-type-icons">
                {item.veg_nonveg === 'VEG' && (
                  <img className='mr-1 h-2 w-2' src={VegIcon} alt="Veg" />
                )}
                {item.veg_nonveg === 'NON' && (
                  <img className='mr-1 h-2 w-2' src={NonVegIcon} alt="Non-Veg" />
                )}
              </div>
              <h1 className="font-semibold text-[14px] break-words w-4/6">{item.name}</h1>
            </div>
            <h1 className="absolute right-4 font-semibold text-[14px]">{item.price}</h1>
          </div>
        ))}
      </div>
    </section>
  )
}

export default MenuSection
