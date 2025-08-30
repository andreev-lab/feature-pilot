<script lang="ts">
  import GitAuth from './GitAuth.svelte';
  import RepoList from './RepoList.svelte';

  import { writable } from 'svelte/store';
  import { onMount } from 'svelte';
  import { GitService } from '../service/git-service';

  const repoList = writable<string[]>([]);
  const isAuthed = writable<boolean>(false);

  function handleRepoList(rp: string[]) {
    repoList.set(rp)
    isAuthed.set(true);
  }

  onMount(() => {
    const authStatusStore = GitService.checkGithubAuth();
    return authStatusStore.subscribe(value => {
      if (value.data?.is_authenticated) {
        isAuthed.set(true);
      }
    });
  });
</script>

<div class="repo-list">
  {#if !$isAuthed}
    <GitAuth onRepoList={handleRepoList}/>
  {:else}
    <RepoList repos={$repoList} />
  {/if}
</div>
