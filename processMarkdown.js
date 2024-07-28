const fs = require('fs');
const markdownIt = require('markdown-it');
const md = new markdownIt();

// Define your variables
const variables = {
  "{{title}}": "Color Set Collections",
  "{{description}}": "Here are some of my favourite colour set collections. Hope you like it."
  "{{color1}}": "#0392cf"
  
};

// Read the Markdown file
const inputFilePath = 'README.md';
let markdownContent = fs.readFileSync(inputFilePath, 'utf-8');

// Replace variables in the Markdown content
for (const [key, value] of Object.entries(variables)) {
  markdownContent = markdownContent.replace(new RegExp(key, 'g'), value);
}

// Convert the Markdown content to HTML (optional)
const htmlContent = md.render(markdownContent);

// Write the processed Markdown or HTML to an output file
const outputFilePath = 'PROCESSED_README.md';
fs.writeFileSync(outputFilePath, markdownContent);

console.log(`Processed Markdown written to ${outputFilePath}`);
