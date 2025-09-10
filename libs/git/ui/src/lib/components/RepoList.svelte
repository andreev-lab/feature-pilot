<script lang="ts">
  import { Button } from '@fp/infra-components';

  export let repos: string[] = [];
</script>


<h4>Repositories:</h4>
<Button>Test</Button>
{#if repos.length}
  <ul>
    {#each repos as repo}
      <li>{repo}</li>
    {/each}
  </ul>
{:else}
  <p>No repos found</p>
{/if}
