// frontend/script.js
document.addEventListener("DOMContentLoaded", () => {
  fetch("http://localhost:8000/api/menu")
    .then((response) => response.json())
    .then((data) => {
      const menuContainer = document.getElementById("menu");
      data.forEach((item) => {
        const menuItem = document.createElement("div");
        menuItem.className = "menu-item";
        menuItem.innerHTML = `
            <h2>${item.name}</h2>
            <p>${item.description}</p>
            <p><strong>Price:</strong> $${item.price}</p>
          `;
        menuContainer.appendChild(menuItem);
      });
    })
    .catch((err) => console.error(err));
});
