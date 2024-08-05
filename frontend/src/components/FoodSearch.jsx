import React, { useState, useEffect } from "react"

function FoodSearch({ menu, onSelectItem }) {
  const [searchTerm, setSearchTerm] = useState("")
  const [filteredItems, setFilteredItems] = useState([])

  useEffect(() => {
    if (searchTerm) {
      const lowercasedTerm = searchTerm.toLowerCase()
      const filtered = menu
        .flatMap((item) => item.subcategory
          ? Object.values(item.subcategory).flat()
          : [])
        .filter((item) => item.title.toLowerCase().includes(lowercasedTerm))
      setFilteredItems(filtered)
    } else {
      setFilteredItems([])
    }
  }, [searchTerm, menu])

  const handleChange = (event) => {
    setSearchTerm(event.target.value)
  }

  const handleSelect = (item) => {
    onSelectItem(item)
    setSearchTerm("")
    setFilteredItems([])
  }

  return (
    <div className="relative">
      <form className="flex gap-2.5 mt-5 text-xs text-center whitespace-nowrap text-neutral-400">
        <div className="flex flex-auto gap-3 self-start px-3 py-2.5 bg-white rounded-[50px]">
          <img
            loading="lazy"
            src="https://cdn.builder.io/api/v1/image/assets/TEMP/0ce52893a6a0c12690dc9c9941da24b422b818047ca0ed8f9f0a80fe9ea47648?apiKey=eb2769a799454c22a06552d614e601b9&&apiKey=eb2769a799454c22a06552d614e601b9"
            alt=""
            className="object-contain shrink-0 w-6 aspect-square"
          />
          <label htmlFor="searchInput" className="sr-only">
            Search
          </label>
          <input
            id="searchInput"
            type="text"
            value={searchTerm}
            onChange={handleChange}
            placeholder="Search"
            className="flex-auto self-start bg-transparent border-none outline-none text-md"
          />
        </div>
        <button type="submit" aria-label="Submit search">
          <img
            loading="lazy"
            src="https://cdn.builder.io/api/v1/image/assets/TEMP/c01b663772da1d03059d8663adc1b0b913e3e683f08497276ee1a1ac819502e8?apiKey=eb2769a799454c22a06552d614e601b9&&apiKey=eb2769a799454c22a06552d614e601b9"
            alt=""
            className="object-contain shrink-0 w-12 rounded-full aspect-square"
          />
        </button>
      </form>
      {filteredItems.length > 0 && (
        <div className="absolute z-10 bg-white border border-gray-300 rounded-lg shadow-lg w-full mt-1">
          {filteredItems.map((item) => (
            <div
              key={item.id}
              className="px-4 py-2 cursor-pointer hover:bg-gray-200"
              onClick={() => handleSelect(item)}
            >
              <div className="flex justify-between">
                <span>{item.title}</span>
                <span>{item.price}</span>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}

export default FoodSearch
