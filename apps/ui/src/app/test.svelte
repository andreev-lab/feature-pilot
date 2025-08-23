<script lang="ts">
  import { svFetch } from '@fp/infra/ui/data';

  const stateStore = svFetch<{ state: number }>('http://0.0.0.0:3000/state');

  async function handleFetch() {
    stateStore.refetch();
  }

  async function handleIncrement() {
    svFetch<{ state: number }>('http://0.0.0.0:3000/state', {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json'
      },
    });
    stateStore.refetch();
  }
</script>

<div>
  <button on:mousedown={handleFetch}>Fetch</button>
  <button on:mousedown={handleIncrement}>Increment</button>

  {#if $stateStore.loading}
    <p>Loading...</p>
  {:else if $stateStore.error}
    <p style="color: red;">
      <span>Error:</span>
      <span>{$stateStore.error.message}</span>
    </p>
  {:else if $stateStore.data}
    <p>
      <span>Server count:</span>
      <span>{$stateStore.data.state}</span>
    </p>
  {/if}
</div>
