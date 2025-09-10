<script lang="ts">
  import { GitService } from '../service/git-service';
  import { navigate } from 'svelte-routing';

  const authCheck = (async () => {
    const isAuthed = await GitService.isAuthed();
    if (!isAuthed) {
      navigate('/auth', { replace: true });
      return false;
    }
    return true;
  })();
</script>

{#await authCheck}
  <h3>Loading...</h3>
{:then isAuthed}
  {#if isAuthed}
    <slot></slot>
  {/if}
{/await}
