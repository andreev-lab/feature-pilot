<script lang="ts">
  import type { Route, RouterOptions } from '@dvcol/svelte-simple-router';
  import { RouterView, RouterDebugger, RouteDebugger } from '@dvcol/svelte-simple-router';
  import { GIT_DEFAULT_ROUTE, GIT_ROUTES } from '@fp/git/ui';
  import AppLayout from './AppLayout.svelte';

  const routes: Readonly<Route<string>[]> = [
    {
      path: '/',
      component: AppLayout,
      children: GIT_ROUTES
    },
    {
      path: '*',
      redirect: {
        name: GIT_DEFAULT_ROUTE.name!
      }
    }
  ]

  const options: RouterOptions = {
    routes
  } as const
</script>

<RouterView {options}>
<!--  <RouterDebugger />-->
<!--  <RouteDebugger />-->
</RouterView>
