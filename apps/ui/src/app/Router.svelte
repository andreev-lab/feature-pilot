<script lang="ts">
  import { Route, Router } from 'svelte-routing';
  import { AuthGuard, GitAuth, UnAuthGuard } from '@fp/git/ui';
  import AppLayout from './AppLayout.svelte';
</script>

<Router>
  <Route path="/auth">
    <UnAuthGuard>
      <GitAuth/>
    </UnAuthGuard>
  </Route>
  <Route>
    <AuthGuard>
      <AppLayout/>
    </AuthGuard>
  </Route>
</Router>
