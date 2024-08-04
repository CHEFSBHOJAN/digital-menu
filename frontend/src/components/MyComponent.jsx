import React, { useState, useEffect } from "react";
import Header from "./Header";
import FoodSearch from "./FoodSearch";
import CategoryTabs from "./CategoryTabs";
import MenuSection from "./MenuSection";

function MyComponent() {
  const [menu, setMenu] = useState([]);
  const [activeCategory, setActiveCategory] = useState("Continental");

  useEffect(() => {
    fetch("http://127.0.0.1:5000/api/getmenu")
      .then((response) => response.json())
      .then((data) => setMenu(data.dishes))
      .catch((error) => console.error("Error fetching menu:", error));
  }, []);

  const handleCategoryChange = (category) => {
    setActiveCategory(category);
  };

  // Filter menu items based on active category
  const filteredMenu = menu.find(
    (item) => item.category.toLowerCase() === activeCategory.toLowerCase()
  );

  return (
    <main className="relative flex overflow-hidden flex-col px-6 py-10 mx-auto w-full tracking-tight max-w-[480px] ">
      <div className=" h-screen w-screen fixed inset-0 -z-10 bg-gradient-to-b from-[#FEEAA0] to-white"></div>
      <Header />
      <h1 className="mt-4 text-lg font-bold text-red-900">
        <span className="text-black">Choose </span>
        <br />
        <span className="text-black">Your Favorite </span>Food
      </h1>
      <FoodSearch />
      <CategoryTabs
        categories={menu.map((item) => item.category)}
        onCategoryChange={handleCategoryChange}
      />
      <h2 className="self-start mt-5 text-xl font-bold text-black">
        {activeCategory}
      </h2>
      <hr className="shrink-0 h-px border-white" />
      <div className="flex flex-col gap-5 mt-2.5 mb-20 w-full">
        {filteredMenu?.subcategory ? (
          Object.keys(filteredMenu.subcategory).map((subcategory, index) => (
            <MenuSection
              key={index}
              title={subcategory}
              items={filteredMenu.subcategory[subcategory]}
            />
          ))
        ) : (
          <div>No items available</div>
        )}
      </div>
    </main>
  );
}

export default MyComponent;
