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
    return svFetch<{ authenticated: boolean }>(`${this.#url}/check-auth`, {
      method: 'GET',
    });
  }

  async isAuthed() {
    try {
      await fpFetch<void>(`${this.#url}/auth`);
      return true;
    } catch (error: unknown) {
      if (!!error && typeof error === 'object' && error instanceof FpFetchError) {
        if (error.response.status === 401) {
          return false
        }
      }
      throw error;
    }
  }
}

export const GitService = new _GitService();
