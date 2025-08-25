export interface CreateLibGeneratorSchema {
  name: string;
  type: 'server' | 'ui';
  domain: string;
}
