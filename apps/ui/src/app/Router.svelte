<script lang="ts">
  import { Route, Router } from 'svelte-routing';
  import { GitAuth } from '@fp/git/ui';
  import AppLayout from './AppLayout.svelte';
</script>

<Router>
  <Route path="/auth" component={GitAuth}/>
  <Route>
    <AppLayout/>
  </Route>
</Router>
