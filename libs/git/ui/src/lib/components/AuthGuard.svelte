<script lang="ts">
  import { GitService } from '../service/git-service';
  import { navigate } from 'svelte-routing';

  const authCheck = (async () => {
    try {
      await GitService.isUserAuthedOrThrow();
      return true
    } catch (e) {
      navigate('/auth', { replace: true });
      return false;
    }
  })();
</script>

{#await authCheck}
  <h3>Loading...</h3>
{:then isAuthed}
  {#if isAuthed}
    <slot></slot>
  {/if}
{/await}
