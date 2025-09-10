import { Layout } from '@fp/layout';
import type {Route} from '@dvcol/svelte-simple-router'

export function layoutRoute(children: Route[]): Readonly<Route> {
  return {
    name: 'layout',
    path: '/',
    component: Layout,
    children
  } as const;
}
