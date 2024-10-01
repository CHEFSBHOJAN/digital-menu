import React, { useState, useEffect, useRef } from "react"
import Loading from "./loading"
import Header from "./Header"
import FoodSearch from "./FoodSearch"
import CategoryTabs from "./CategoryTabs"
import MenuSection from "./MenuSection"
import SpecialDishes from "./Special"

function MyComponent({ outlet }) {
  const [menu, setMenu] = useState([])
  const [activeCategory, setActiveCategory] = useState("Starters")
  const itemRefs = useRef({})
  const [loading, setLoading] = useState(false)

  useEffect(() => {
    setLoading(true)
    let url
    if (outlet === "Dhavali") {
      url = "https://digital-menu-6maa.onrender.com/api/getmenumargao"
    }
    else {
      url = "https://digital-menu-6maa.onrender.com/api/getmenuponda"
    }
    fetch(url)
      .then((response) => response.json())
      .then((data) => {
        setMenu(data.dishes)
        setLoading(false)
      })
      .catch((error) => {
        console.error("Error fetching menu:", error)
        setLoading(false)
      })
  }, [])


  const handleCategoryChange = (category) => {
    setActiveCategory(category)
  }

  const handleItemSelect = (item) => {
    const itemCategory = menu.find(
      (cat) => Object.values(cat.subcategory).flat().some((i) => i.id === item.id)
    )

    if (itemCategory) {
      setActiveCategory(itemCategory.category)

      setTimeout(() => {
        const itemRef = itemRefs.current[item.id]
        if (itemRef) {
          itemRef.scrollIntoView({
            behavior: "smooth",
            block: "center",
            inline: "nearest"
          })
        }
      }, 100)
    }
  }

  const todaysSpecialItems = menu
    .filter(item => item.category.toLowerCase() === "special")
    .flatMap(item => item.subcategory["TODAYS SPECIAL"] || [])

  console.log(todaysSpecialItems)

  const filteredMenu = menu.find(
    (item) => item.category.toLowerCase() === activeCategory.toLowerCase()
  )

  return (
    <main className="relative flex overflow-hidden flex-col px-6 py-10 mx-auto w-screen tracking-tight max-w-[480px] ">
      <div className=" h-screen w-screen fixed inset-0 -z-10 bg-gradient-to-b from-[#FEEAA0] to-white"></div>
      <Header outletName={outlet} />
      <h1 className="mt-4 text-lg font-bold text-red-900">
        <span className="text-black">Choose </span>
        <br />
        <span className="text-black">Your Favorite </span>Food
      </h1>
      <FoodSearch menu={menu} onSelectItem={handleItemSelect} />
      <SpecialDishes specialDishes={todaysSpecialItems} />
      <CategoryTabs
        categories={menu.map((item) => item.category)}
        activeCategory={activeCategory}
        onCategoryChange={handleCategoryChange}
      />
      <h2 className="self-start mt-5 text-xl font-bold text-black">
        {activeCategory.charAt(0).toUpperCase() + activeCategory.slice(1).toLowerCase()}
      </h2>
      <hr className="shrink-0 h-px border-white" />
      {loading ? (
        <div className="w-full flex justify-center items-center">
          <Loading />
        </div>
      ) : (
        <div className="flex flex-col gap-5 mt-2.5 mb-20 w-full">
          {filteredMenu?.subcategory ? (
            Object.keys(filteredMenu.subcategory).map((subcategory, index) => (
              <MenuSection
                key={index}
                title={subcategory}
                items={filteredMenu.subcategory[subcategory]}
                itemRefs={itemRefs}
              />
            ))
          ) : (
            <div>No items available</div>
          )}
        </div>
      )}
    </main >
  )
}

export default MyComponent
