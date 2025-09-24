<script lang="ts">
  import RepoList from './RepoList.svelte';
  import { writable } from 'svelte/store';

  const repoList = writable<string[]>([]);
</script>

<div class="repo-list">
  <RepoList repos={$repoList} />
</div>
