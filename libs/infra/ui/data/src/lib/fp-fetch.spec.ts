import { describe, it, expect, vi, afterEach } from 'vitest';
import { fpFetch, FpFetchError } from './fp-fetch';

describe('fpFetch', () => {
  afterEach(() => {
    vi.restoreAllMocks();
  });

  it('should return JSON body on successful request', async () => {
    const mockData = { message: 'Success' };
    const mockResponse = {
      ok: true,
      json: () => new Promise((resolve) => resolve(mockData)),
    };
    vi.stubGlobal('fetch', vi.fn().mockResolvedValue(mockResponse));

    const data = await fpFetch('http://test.com');

    expect(data).toEqual(mockData);
    expect(fetch).toHaveBeenCalledWith('http://test.com', undefined);
  });

  it('should throw FpFetchError on a failed request', async () => {
    const mockResponse = {
      ok: false,
      status: 404,
      statusText: 'Not Found',
    };
    vi.stubGlobal('fetch', vi.fn().mockResolvedValue(mockResponse));

    await expect(fpFetch('http://test.com')).rejects.toThrow(FpFetchError);
  });

  it('should have response property in FpFetchError', async () => {
    const mockResponse = {
      ok: false,
      status: 404,
      statusText: 'Not Found',
    };
    vi.stubGlobal('fetch', vi.fn().mockResolvedValue(mockResponse));

    try {
      await fpFetch('http://test.com');
    } catch (error) {
      if (error instanceof FpFetchError) {
        expect(error.response).toBe(mockResponse);
      }
    }
  });
});
