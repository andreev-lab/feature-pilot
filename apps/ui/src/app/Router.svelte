<script lang="ts">
  import type { Route, RouterOptions } from '@dvcol/svelte-simple-router';
  import {RouterView} from '@dvcol/svelte-simple-router';
  import { GitPage } from '@fp/git/ui';

  const routes: Readonly<Route<string>[]> = [
    {
      name: 'root',
      path: '/',
      component: GitPage
    }
  ]

  const options: RouterOptions = {
    routes
  } as const
</script>

<RouterView {options}/>

