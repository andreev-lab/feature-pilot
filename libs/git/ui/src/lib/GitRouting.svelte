<script>
  import { Route } from 'svelte-routing';
  import GitPage from './GitPage.svelte';
  import { Redirect } from '@fp/infra/ui/data';
</script>

<Route path="/project">
  <GitPage />
</Route>
<Route>
  <Redirect to="/project"/>
</Route>
