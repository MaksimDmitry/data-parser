const fs = require('fs');
const path = require('path');

class Parser {
  constructor(filePath) {
    this.filePath = filePath;
    this.data = [];
  }

  async readData() {
    try {
      const rawData = await fs.promises.readFile(this.filePath, 'utf8');
      return rawData;
    } catch (error) {
      throw new Error(`Error reading file: ${error.message}`);
    }
  }

  parseData(rawData) {
    const lines = rawData.split('\n');
    lines.forEach((line) => {
      const trimmedLine = line.trim();
      if (trimmedLine) {
        const parsedLine = trimmedLine.split(',');
        this.data.push(parsedLine);
      }
    });
    return this.data;
  }

  async processData() {
    const rawData = await this.readData();
    return this.parseData(rawData);
  }
}

module.exports = Parser;