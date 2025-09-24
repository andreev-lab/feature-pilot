<script lang="ts">
  import { navigate } from 'svelte-routing';
  import { isUserAuthenticated } from './is-user-authenticated';

  const authCheck = (async () => {
    const auth = await isUserAuthenticated();
    if (!auth) {
      console.log('Nav');
      navigate('/auth', { replace: true });
    }
    return auth
  })();
</script>

{#await authCheck}
  <h3>Thinking...</h3>
{:then isAuthed}
  {#if isAuthed}
    <slot></slot>
  {/if}
{/await}
