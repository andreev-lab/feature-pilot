<script lang="ts">
  import { navigate } from 'svelte-routing';
  import { isUserAuthenticated } from './is-user-authenticated';

  const authCheck = (async () => {
    const auth = isUserAuthenticated()
    if (auth) {
      navigate('/', { replace: true });
    }
    return auth
  })();
</script>

{#await authCheck}
  <h3>Thinking...</h3>
{:then isAuthed}
  {#if !isAuthed}
    <slot></slot>
  {/if}
{/await}
