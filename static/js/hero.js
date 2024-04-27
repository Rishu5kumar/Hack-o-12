// Function to initialize Google Translate Element
// function googleTranslateElementInit() {
//     new google.translate.TranslateElement({
//         pageLanguage: 'en',
//         includedLanguages: 'en,fr,es', // Include the languages you want to support
//         layout: google.translate.TranslateElement.InlineLayout.SIMPLE
//     }, 'google_translate_element');
// }
// googleTranslateElementInit();

// JavaScript to show social media icons when hovering over the social media icon
const socialMediaIcon = document.getElementById('socialMediaIcon');
const socialMediaDropdown = document.getElementById('socialMediaDropdown');

socialMediaIcon.addEventListener('mouseenter', () => {
    socialMediaDropdown.style.display = 'block';
    socialMediaDropdown.style.top = `${socialMediaIcon.offsetHeight}px`;

});

socialMediaIcon.addEventListener('mouseleave', () => {
    socialMediaDropdown.style.display = 'none';
});