 document.addEventListener("DOMContentLoaded", function () {
     //   for the menu
  const menuToggle = document.getElementById('menu-toggle');
  const mobileMenu = document.getElementById('mobile-menu');

  menuToggle.addEventListener('click', () => {
    mobileMenu.classList.toggle('hidden');


  });


    // Contact form submission handler
    document.getElementById("contactForm").addEventListener("submit", function (e) {
      e.preventDefault();

      const name = document.getElementById("name").value.trim();
      const email = document.getElementById("email").value.trim();
      const message = document.getElementById("message").value.trim();
      const formMessage = document.getElementById("formMessage");

      //  Basic validation
      if (!name || !email || !message) {
        formMessage.textContent = " Please fill in all fields.";
        formMessage.style.color = "red";
        return;
      }

      //  Email validation
      const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailPattern.test(email)) {
        formMessage.textContent = "📧 Please enter a valid email address.";
        formMessage.style.color = "red";
        return;
      }

      //  Get existing data or initialize empty array
      const contactFormData = JSON.parse(localStorage.getItem("contactFormData")) || [];

      //  Add new entry to the list
      contactFormData.push({ name, email, message });

      //  Save to localStorage
      localStorage.setItem("contactFormData", JSON.stringify(contactFormData));

      formMessage.textContent = " Thank you! Your message has been saved.";
      formMessage.style.color = "green";

      document.getElementById("contactForm").reset();
    });

   
  });