<script lang="ts">
  import type { Snippet } from 'svelte';
  let { children, sidebar }: { children: Snippet, sidebar: Snippet } = $props();
</script>

<div class="layout">
  {@render sidebar?.()}
  <main class="main-content">
    {@render children?.()}
  </main>
</div>

<style lang="scss">
  .layout {
    display: flex;
    height: 100vh;
    background-color: #f4f7fa;
  }

  .main-content {
    flex-grow: 1;
    padding: 1rem;
    overflow-y: auto;
  }
</style>
