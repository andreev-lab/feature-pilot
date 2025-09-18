<script lang="ts">
  import type { Snippet } from 'svelte';
  import Sidebar from './Sidebar.svelte';

  let { children }: { children: Snippet } = $props();
</script>

<div class="layout">
  <Sidebar />
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
