/*
const svgContainer = document.querySelector(".landing-svg-container")
const svg = document.querySelector(".landing-svg")
console.log(svg)
const logo = document.querySelector(".landing-logo")
console.log(logo)
if(innerWidth <= 1330){
    // svgContainer.innerHTML = ``
    console.log(svg.style)
    svg.style.left = "0"
    svg.style.width = "150vh"
    // logo.style.display = "None"
}
*/
// Mobile navbar Functionality
const mobileNavBtn = document.querySelector(".mobile-navbar-btn")
const mobileNavBg = document.querySelector(".mobile-navbar-background")
const mobileNav = document.querySelector(".mobile-navbar-nav")
const mobileNavLink = document.querySelector(".mobile-navbar-link")
const mobileNavIvon = document.querySelector(".mobile-navbar-icon")
const mobileNavIvonBef = document.querySelector(".mobile-navbar-icon::before")
const mobileNavIvonAft = document.querySelector(".mobile-navbar-icon::after")

mobileNavBtn.addEventListener("click",()=>{
    mobileNavBg.classList.toggle("toggle")
    mobileNav.classList.toggle("toggle")
    mobileNavIvon.classList.toggle("toggle")
})