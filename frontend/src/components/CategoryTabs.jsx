import React from "react"

function CategoryTabs({ categories, activeCategory, onCategoryChange }) {
  return (
    <nav className="scroll-container flex gap-1 mt-3.5 py-2 px-2 text-xs font-medium text-black space-x-2 whitespace-nowrap overflow-x-scroll">
      {categories.map((category, index) => (
        <button
          key={index}
          onClick={() => onCategoryChange(category)}
          className={`px-4 py-2 rounded-[50px] shadow-[0px_1px_5px_rgba(0,0,0,0.25)] ${category === activeCategory ? "bg-red-900 text-white" : "bg-white"
            }`}
        >
          {category}
        </button>
      ))}
    </nav>
  )
}

export default CategoryTabs
