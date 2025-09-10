<script lang="ts">
  import type { Route, RouterOptions } from '@dvcol/svelte-simple-router';
  import { Layout } from '@fp/layout';
  import { RouterView, RouterDebugger, RouteDebugger } from '@dvcol/svelte-simple-router';
  import { GIT_ROUTES } from '@fp/git/ui';
  import Router from './Router.svelte';

  const routes: Readonly<Route<string>[]> = [...GIT_ROUTES]

  const options: RouterOptions = {
    routes,
    base: '/',
  } as const
</script>

<Layout>
  <RouterView name="Nested" {options}/>
</Layout>
