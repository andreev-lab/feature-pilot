import type { Route } from '@dvcol/svelte-simple-router';
import {default as GitAuth} from './components/GitAuth.svelte';
import {default as GitPage} from './GitPage.svelte'
import { GitService } from './service/git-service';

type GitRouteNames = 'auth' | 'project';

export const GIT_ROUTES: Readonly<Route<GitRouteNames>[]> = [
  {
    name: 'auth',
    path: '/auth',
    component: GitAuth,
    beforeEnter: async () =>
      await GitService.isAuthed() ? { name: 'project' } : { name: 'auth' },
  },
  {
    name: 'project',
    path: '/project',
    component: GitPage,
    beforeEnter: async () =>
      await GitService.isAuthed() ? { name: 'project' } : { name: 'auth' },
  },
];

export const GIT_DEFAULT_ROUTE = GIT_ROUTES[0];
