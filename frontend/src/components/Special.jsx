
import React from "react"

function SpecialDishes({ specialDishes }) {
    console.log(specialDishes)

    if (!specialDishes || specialDishes.length === 0) {
        return null
    }

    return (
        <div className="special-dishes-container overflow-hidden py-2">
            <h2 className="text-lg font-bold text-center text-red-900 mb-2">Today's Special</h2>
            <div className="special-dishes-carousel flex gap-4 overflow-x-auto">
                {specialDishes.map((dish, index) => (
                    <div
                        key={index}
                        className="special-dish-card bg-gradient-to-br from-yellow-50 via-white to-red-100 shadow-lg rounded-lg flex-shrink-0 w-48 transform transition duration-300 hover:scale-105"
                    >
                        <div className="p-2">
                            <h3 className="text-sm font-semibold text-gray-900">{dish.name}</h3>
                            <p className="text-xs text-gray-600 mt-1">{dish.description}</p>
                            <p className="text-sm font-bold text-red-600 mt-2">₹{dish.price}</p>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    )
}

export default SpecialDishes
