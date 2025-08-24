import { writable } from 'svelte/store';
import { fpFetch, FpFetchError } from './fp-fetch';

export function svFetch<T>(input: RequestInfo | URL, init?: RequestInit) {
  const { subscribe: storeSubscribe, set, update } = writable<{ data: T | null; loading: boolean; error: FpFetchError | null }>({
    data: null,
    loading: true,
    error: null,
  });

  let controller: AbortController | null = null;

  const fetchData = async () => {
    if (controller) {
      controller.abort();
    }
    controller = new AbortController();
    const signal = controller.signal;

    set({ data: null, loading: true, error: null });
    try {
      const result = await fpFetch<T>(input, { ...init, signal });
      set({ data: result, loading: false, error: null });
    } catch (e) {
      if (e instanceof DOMException && e.name === 'AbortError') {
        set({ data: null, loading: false, error: null });
      } else if (e instanceof FpFetchError) {
        set({ data: null, loading: false, error: e });
      } else {
        set({ data: null, loading: false, error: new FpFetchError(new Response(null, { status: 500 }), (e as Error).message) });
      }
    } finally {
      controller = null;
    }
  };

  fetchData();

  return {
    subscribe(run: (value: { data: T | null; loading: boolean; error: FpFetchError | null }) => void) {
      const unsubscribe = storeSubscribe(run);
      return () => {
        unsubscribe();
        if (controller) {
          controller.abort();
        }
      };
    },
    refetch: fetchData,
  };
}
