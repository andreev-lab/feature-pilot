<script lang="ts">
  export let repos: string[] = [];
</script>


<h4>Repositories:</h4>
{#if repos.length}
  <ul>
    {#each repos as repo}
      <li>{repo}</li>
    {/each}
  </ul>
{:else}
  <p>No repos found</p>
{/if}
