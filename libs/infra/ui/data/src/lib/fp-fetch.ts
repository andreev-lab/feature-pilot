export class FpFetchError extends Error {
  constructor(
    public readonly response: Response,
    message?: string,
  ) {
    super(message ?? `Request failed with status ${response.status}`);
  }
}

export async function fpFetch<T>(input: RequestInfo | URL, init?: RequestInit): Promise<T> {
  const response = await fetch(input, init);

  if (!response.ok) {
    throw new FpFetchError(response);
  }

  return response.json() as Promise<T>;
}