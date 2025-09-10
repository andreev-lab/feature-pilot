<script>
  import { Route, Router } from 'svelte-routing';
  import GitPage from './GitPage.svelte';
  import { Redirect } from '@fp/infra/ui/data';
  import { AuthGuard } from './components/index.js';
</script>

<Router>
  <Route path="/project">
    <AuthGuard>
      <GitPage />
    </AuthGuard>
  </Route>
  <Route>
    <Redirect to="/project"/>
  </Route>
</Router>
