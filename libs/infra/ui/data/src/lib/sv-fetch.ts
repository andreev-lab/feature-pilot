import { writable } from 'svelte/store';
import { fpFetch, FpFetchError } from './fp-fetch'; // Assuming fp-fetch.ts is in the same directory

export function svFetch<T>(input: RequestInfo | URL, init?: RequestInit) {
  const { subscribe, set, update } = writable<{ data: T | null; loading: boolean; error: FpFetchError | null }>({
    data: null,
    loading: true,
    error: null,
  });

  const fetchData = async () => {
    set({ data: null, loading: true, error: null });
    try {
      const result = await fpFetch<T>(input, init);
      set({ data: result, loading: false, error: null });
    } catch (e) {
      if (e instanceof FpFetchError) {
        set({ data: null, loading: false, error: e });
      } else {
        set({ data: null, loading: false, error: new FpFetchError(new Response(null, { status: 500 }), (e as Error).message) });
      }
    }
  };

  fetchData();

  return {
    subscribe,
    refetch: fetchData,
  };
}
