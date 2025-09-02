<script lang="ts">
  import type { Route, RouterOptions } from '@dvcol/svelte-simple-router';
  import { RouterView } from '@dvcol/svelte-simple-router';
  import { GIT_DEFAULT_ROUTE, GIT_ROUTES } from '@fp/git/ui';

  const routes: Readonly<Route<string>[]> = [
    ...GIT_ROUTES,
    {
      path: '*',
      redirect: {
        name: GIT_DEFAULT_ROUTE.name
      }
    },
    {
      path: '/',
      redirect: {
        name: GIT_DEFAULT_ROUTE.name
      }
    }
  ]

  const options: RouterOptions = {
    routes
  } as const
</script>

<RouterView {options}/>

