import React from "react";

function MenuSection({ title, items }) {
  return (
    <section className="flex flex-col flex-1 self-start">
      <h3 className="text-lg font-medium text-red-900">{title}</h3>
      <div className="flex gap-5 justify-between self-start mt-2.5 text-xs leading-4 text-black">
        <div className="space-y-2">
          {items.map((item) => (
            <div key={item.id} className="space-y-2">
              <div className=" w-screen relative flex py-2">
                <h1 className=" font-semibold text-[14px] absolute tracking-wide left-2">{item.name}</h1>
                <h1 className=" font-semibold text-[14px] absolute right-12">{item.price}</h1>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

export default MenuSection;
