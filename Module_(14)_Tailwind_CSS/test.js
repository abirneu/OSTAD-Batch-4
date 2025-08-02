const menu = document.querySelector("#menu");
const menu_list = document.querySelector("#menu_list");

menu.addEventListener("click", () => {
    menu_list.classList.toggle("hidden");
    menu.classList.toggle("bg-white");
});