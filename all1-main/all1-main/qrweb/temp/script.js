const generateBtn = document.getElementById('generateBtn');
const displayBtn = document.getElementById('displayBtn');
const contentDiv = document.getElementById('content');

// Sample content to generate
const sampleContent = [
  {
    text: "Check out this amazing product!",
    image: "https://via.placeholder.com/300" // Replace with your product photo
  },
  {
    text: "New collection just arrived!",
    image: "https://via.placeholder.com/300" // Replace with your product photo
  },
  {
    text: "Limited time offer!",
    image: "https://via.placeholder.com/300" // Replace with your product photo
  }
];

generateBtn.addEventListener('click', () => {
  // Randomly select content
  const randomIndex = Math.floor(Math.random() * sampleContent.length);
  const generatedContent = `
    <p>${sampleContent[randomIndex].text}</p>
    <img src="${sampleContent[randomIndex].image}" alt="Product Photo" class="product-image">
  `;
  contentDiv.innerHTML = generatedContent;
  contentDiv.classList.remove('hidden');
  contentDiv.classList.add('fade-in');
});

displayBtn.addEventListener('click', () => {
  // Display the generated content
  if (contentDiv.innerHTML !== "") {
    contentDiv.classList.remove('hidden');
    contentDiv.classList.add('fade-in');
  } else {
    alert("Generate content first!");
  }
});