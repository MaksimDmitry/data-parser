const fs = require('fs');
const path = require('path');

class DataParser {
  constructor(filePath) {
    this.filePath = filePath;
    this.data = null;
  }

  async readFile() {
    try {
      const content = await fs.promises.readFile(this.filePath, 'utf8');
      return content;
    } catch (error) {
      throw new Error(`Failed to read file: ${error.message}`);
    }
  }

  async parseData() {
    const fileContent = await this.readFile();
    const lines = fileContent.split('\n');
    const parsedData = lines.map((line) => line.trim().split(','));
    this.data = parsedData;
    return this.data;
  }

  async saveToJSON(outputFilePath) {
    if (!this.data) {
      throw new Error('No data to save');
    }
    try {
      const jsonData = JSON.stringify(this.data, null, 2);
      await fs.promises.writeFile(outputFilePath, jsonData);
    } catch (error) {
      throw new Error(`Failed to save JSON file: ${error.message}`);
    }
  }
}

async function main() {
  const parser = new DataParser(path.join(__dirname, 'data.csv'));
  const parsedData = await parser.parseData();
  console.log(parsedData);
  await parser.saveToJSON(path.join(__dirname, 'output.json'));
}

main().catch((error) => console.error(error));