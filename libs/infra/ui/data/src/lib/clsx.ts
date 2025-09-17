type ClassValue = ClassArray | ClassDictionary | string | number | bigint | null | boolean | undefined;
type ClassDictionary = Record<string, any>;
type ClassArray = ClassValue[];

export function clsx(...classNames: ClassValue[]) {
  return classNames
}
