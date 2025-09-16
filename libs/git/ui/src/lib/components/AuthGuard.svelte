<script lang="ts">
  import { GitService } from '../service/git-service';
  import { navigate } from 'svelte-routing';

  const authCheck = (async () => {
    try {
      const {is_authenticated} = await GitService.checkGithubAuth();
      if (!is_authenticated) {
        navigate('/auth', { replace: true });
        return false;
      }
      return true
    } catch (e) {
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
