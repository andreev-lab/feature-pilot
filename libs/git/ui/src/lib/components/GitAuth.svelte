<script lang="ts">
  import { writable } from 'svelte/store';
  import { GitService } from '../service/git-service';
  import { env } from '@fp/infra/ui/data';

  export let onRepoList: ((repoList: string[]) => void) | undefined = undefined;

  let org: string = '';
  let pat: string = '';

  const fetchOptions = writable<{ org: string; pat: string } | null>(null);
  const gitService = GitService;

  $: repoFetch = $fetchOptions ? gitService.getRepoList($fetchOptions) : null;

  $: repos = $repoFetch?.data?.repos || [];
  $: loading = $repoFetch?.loading || false;
  $: error = $repoFetch?.error ? $repoFetch.error.message : null;
  if (repos && onRepoList) {
    onRepoList(repos);
  }

  function fetchRepos() {
    fetchOptions.set({ org, pat });
  }

  function handleGithubLogin() {
    window.location.href = `${env.serverUrl}/git/login/github`;
  }
</script>

<style>
  .repo-list {
    /* Add styles for the repository list */
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
    max-width: 600px;
    margin: 20px auto;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }

  .repo-list h3 {
    text-align: center;
    color: #333;
    margin-bottom: 20px;
  }

  .form-group {
    margin-bottom: 15px;
  }

  .form-group label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
    color: #555;
  }

  .form-group input[type="text"],
  .form-group input[type="password"] {
    width: calc(100% - 20px);
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 16px;
  }

  .form-group input[type="text"]:focus,
  .form-group input[type="password"]:focus {
    border-color: #007bff;
    outline: none;
    box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
  }

  button {
    display: block;
    width: 100%;
    padding: var(--fp-distance-2) var(--fp-distance-4);
    background-color: var(--fp-color-blue);
    color: var(--fp-color-text-secondary);
    border: none;
    border-radius: var(--fp-border-radius);
    cursor: pointer;
    transition: background-color 0.2s ease-in-out;
  }

  button:hover {
    background-color: #0056b3;
  }

  button:disabled {
    background-color: #cccccc;
    cursor: not-allowed;
  }

  .message {
    margin-top: 20px;
    padding: 10px;
    border-radius: 4px;
    text-align: center;
  }

  .message.error {
    background-color: #f8d7da;
    color: #721c24;
    border: 1px solid #f5c6cb;
  }

  .message.loading {
    background-color: #e2e3e5;
    color: #383d41;
    border: 1px solid #d6d8db;
  }


</style>

<div class="repo-list">
  <h3>Git Auth</h3>

  <form on:submit|preventDefault={fetchRepos}>
    <div class="form-group">
      <label for="org">Organization:</label>
      <input type="text" id="org" bind:value={org} required />
    </div>
    <div class="form-group">
      <label for="pat">Personal Access Token:</label>
      <input type="password" id="pat" bind:value={pat} required />
    </div>
    <button type="submit" disabled={loading}>
      {#if loading}
        Fetching...
      {:else}
        Fetch Repos
      {/if}
    </button>
  </form>

  <button on:click={handleGithubLogin}>
    Login with GitHub
  </button>

  {#if error}
    <p class="message error">{error}</p>
  {:else if loading}
    <p class="message loading">Loading repositories...</p>
  {/if}
</div>
