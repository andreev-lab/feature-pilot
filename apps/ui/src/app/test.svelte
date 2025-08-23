<script lang="ts">
  import { fpFetch, FpFetchError } from '@fp/infra/ui/data';

  let res = $state<{ count: number; } | null>(null);
  let error = $state<FpFetchError | null>(null);

  function setState({state}: {state: number}) {
    res = {
      count: state
    }
    error = null;
  }

  function setError(err: FpFetchError) {
    error = err
    res = null;
  }

  async function handleFetch() {
    try {
      const stateRes = await fpFetch<{state: number}>('http://0.0.0.0:3000/state');
      setState(stateRes);
    } catch (e) {
      setError(e);
    }
  }

  async function handleIncrement() {
    try {
      const stateRes = await fpFetch<{state: number}>('http://0.0.0.0:3000/state', {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json'
        },
      });
      setState(stateRes);
    } catch (e) {
      setError(e);
    }
  }
</script>

<div>
  <button on:mousedown={handleFetch}>Fetch</button>
  <button on:mousedown={handleIncrement}>Increment</button>
  {#if error}
    <p style="color: red;">
      <span>Error:</span>
      <span>{error}</span>
    </p>
  {:else }
    <p>
      <span>Server count:</span>
      <span>{res?.count}</span>
    </p>
  {/if}
</div>


