import { env, fpFetch, svFetch } from '@fp/infra/ui/data';

class _GitService {
  #url = `${env.serverUrl}/git`;

  getRepoList(params: {org: string, pat: string}) {
    return svFetch<{ repos: string[] }>(`${this.#url}/list-repos`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(params),
    })
  }

  isUserAuthedOrThrow() {
    return fpFetch<{ is_authenticated: boolean }>(`${this.#url}/auth`, {
      method: 'GET',
    });
  }

  logout() {
    return fpFetch(`${this.#url}/logout`, { method: 'GET' });
  }
}

export const GitService = new _GitService();
