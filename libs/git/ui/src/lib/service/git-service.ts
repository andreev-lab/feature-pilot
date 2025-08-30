import { env, svFetch } from '@fp/infra/ui/data';
class _GitService {
  #url = env.serverUrl;

  getRepoList(params: {org: string, pat: string}) {
    return svFetch<{ repos: string[] }>(`${this.#url}/git/list-repos`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(params),
    })
  }
  checkGithubAuth() {
    return svFetch<{ authenticated: boolean }>(`${this.#url}/git/check-auth`, {
      method: 'GET',
    });
  }
}

export const GitService = new _GitService();
