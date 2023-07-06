const puppeteer = require('puppeteer');

async function scrapeData() {
  const browser = await puppeteer.launch({ headless: 'new'});
  const page = await browser.newPage();
  
  // URL of the webpage
  const url = 'https://seekingalpha.com/symbol/CRWD/earnings';

  await page.goto(url); // Wait for network connections to settle

  // Extract the desired data from the page using DOM manipulation or other techniques
  const data = await page.evaluate(() => {
    const elements = document.querySelectorAll('*'); // Select all elements on the page
    for (let i = 0; i < elements.length; i++) {
      if (elements[i].textContent.includes('Your Target String')) {
        return elements[i].textContent;
      }
    }
    return 'Element not found.';
  });

  console.log(data);

  await browser.close();
}

scrapeData();
