<script lang="ts">
  import RepoSelector from './components/RepoSelector.svelte';
  import ReadmeDisplay from './components/ReadmeDisplay.svelte';
</script>

<style>
  .git-page-container {
    display: flex;
    height: 100%;
  }

  .right-panel,
  .left-panel {
    padding: var(--fp-distance-2) var(--fp-distance-4);
    background-color: var(--fp-color-background);
  }

  .left-panel {
    flex: 1;
    border-right: var(--fp-border);
  }

  .right-panel {
    flex: 3;
  }
</style>

<div class="git-page-container">
  <div class="left-panel">
    <RepoSelector />
  </div>
  <div class="right-panel">
    <ReadmeDisplay />
  </div>
</div>
