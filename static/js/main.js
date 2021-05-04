/* jQuery for javascript initialization */

$(document).ready(function () {
   $('.collapse').collapse();
});


const parallax = document.getElementById("block-one");

window.addEventListener("scroll", function()
{
   let offset = window.pageYOffset;
   parallax.style.backgroundPositionY = `${offset * 0.7}px`;
})

