// types.ts
export interface DataRecord {
  id: number;
  name: string;
  createdAt: Date;
}

export interface ParsedData {
  records: DataRecord[];
  errors: string[];
}

export type ParseStatus = 'success' | 'failure';

export interface ParserConfig {
  filePath: string;
  delimiter: string;
  skipHeader: boolean;
}

export class ParsingError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'ParsingError';
  }
}