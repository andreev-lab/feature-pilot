<script>
  import { Route, Router } from 'svelte-routing';
  import GitPage from './GitPage.svelte';
  import { Redirect } from '@fp/infra/ui/data';
</script>

<Router>
  <Route path="/project">
    <GitPage />
  </Route>
  <Route>
    <Redirect to="/project"/>
  </Route>
</Router>
