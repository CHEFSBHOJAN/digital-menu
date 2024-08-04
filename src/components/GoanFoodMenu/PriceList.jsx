/**
 * This code was generated by Builder.io.
 */
import React from "react";

function PriceList({ prices }) {
  return (
    <ul className="flex flex-col text-xs text-black">
      {prices.map((price, index) => (
        <li key={index} className="leading-4">
          {price}
        </li>
      ))}
    </ul>
  );
}

export default PriceList;
