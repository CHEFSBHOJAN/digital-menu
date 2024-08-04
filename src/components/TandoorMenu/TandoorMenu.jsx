/**
 * This code was generated by Builder.io.
 */
import React from "react";
import Header from "./Header";
import SearchBar from "./SearchBar";
import CategoryTabs from "./CategoryTabs";
import MenuSection from "./MenuSection";

function TandoorMenu() {
  const categories = [
    { name: "Continental", active: false },
    { name: "Asian", active: false },
    { name: "Chinese", active: false },
    { name: "Tandoor", active: true },
    { name: "Indian", active: false },
    { name: "Goan", active: false },
  ];

  const menuSections = [
    {
      title: "Grilled",
      items: [
        { name: "Tandoori Chicken Full", price: "Rs 440" },
        { name: "Tandoori Chicken Half", price: "Rs 250" },
        { name: "Grilled Mushroom TIkka", price: "Rs 240" },
        { name: "Tandoori Broccoli", price: "Rs 270" },
        { name: "Tandoori Baby Corn", price: "Rs 270" },
        { name: "Tandoori Gobi", price: "Rs 210" },
        { name: "Tandoori Wings", price: "Rs 260" },
        { name: "Chicken Afghani Kebab", price: "Rs 290" },
        { name: "Grilled Chicken Lolypop", price: "Rs 240" },
        { name: "Tandoori Grilled Prawns", price: "Rs 390" },
        { name: "Grilled Mackrel", price: "Rs 170" },
        { name: "Tandoori Malai Brocolli", price: "Rs 240" },
      ],
    },
    {
      title: "Kebab",
      items: [
        { name: "Tangdai Kebab", price: "Rs 290" },
        { name: "Malai Kebab", price: "Rs 320" },
        { name: "Haryani Chicken Tikka", price: "Rs 289" },
        { name: "Chicken Shish Taouk", price: "Rs 289" },
        { name: "Chicken TIkka", price: "Rs 280" },
        { name: "Chicken Seekh Kabab", price: "Rs 285" },
        { name: "Mutthon Seekh Kabab", price: "Rs 350" },
        { name: "Paneer Haryani Kabab", price: "Rs 260" },
        { name: "Paneer Tikka", price: "Rs 250" },
        { name: "Paneer Malai Tikka", price: "Rs 270" },
        { name: "Veg Seekh Kebab", price: "Rs 220" },
      ],
    },
    {
      title: "Roti",
      items: [
        { name: "Tandoori Roti", price: "Rs 15" },
        { name: "Butter Roti", price: "Rs 15" },
        { name: "Butter Naan", price: "Rs 35" },
        { name: "Plain Naan", price: "Rs 25" },
        { name: "Cheese Garlic Naan", price: "Rs 120" },
        { name: "Tandoori Butter Paratha", price: "Rs 35" },
      ],
    },
    {
      title: "Starters",
      items: [
        { name: "Tandoori Plain Paratha", price: "Rs 25" },
        { name: "Garlic Naan", price: "Rs 45" },
        { name: "Onion Butter Kulcha", price: "Rs 45" },
        { name: "Butter Garlic Naan", price: "Rs 45" },
      ],
    },
  ];

  return (
    <main className="flex overflow-hidden flex-col px-6 py-12 mx-auto w-full tracking-tight max-w-[480px]">
      <Header />
      <h1 className="mt-4 text-lg font-bold text-red-900">
        <span className="text-black">Choose </span>
        <br />
        <span className="text-black">Your Favorite </span>Food
      </h1>
      <SearchBar />
      <CategoryTabs categories={categories} />
      <h2 className="self-start mt-5 text-base font-bold text-black">
        Tandoor
      </h2>
      <hr className="shrink-0 h-px mt-2.5" />
      {menuSections.map((section, index) => (
        <MenuSection key={index} title={section.title} items={section.items} />
      ))}
    </main>
  );
}

export default TandoorMenu;
