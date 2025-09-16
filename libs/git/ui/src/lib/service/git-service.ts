import { env, fpFetch, FpFetchError, svFetch } from '@fp/infra/ui/data';
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

  checkGithubAuth() {
    return fpFetch<{ is_authenticated: boolean }>(`${this.#url}/check-auth`, {
      method: 'GET',
    });
  }
}

export const GitService = new _GitService();
