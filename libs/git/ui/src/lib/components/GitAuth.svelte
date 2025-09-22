<script lang="ts">
  import { env } from '@fp/infra/ui/data';
  import { Button } from '@fp/infra/components';
  import { GithubIcon, GitlabIcon } from '@lucide/svelte/icons';
  import ButbucketIcon from './icon/ButbucketIcon.svelte';

  function handleGithubLogin() {
    window.location.href = `${env.serverUrl}/git/login/github`;
  }

  function handleGitlabLogin() {
    console.log('GitLab login clicked (disabled)');
  }

  function handleBitbucketLogin() {
    console.log('Bitbucket login clicked (disabled)');
  }
</script>

<main class="height-100 center-text flex column gap-lg ">
  <h3>Git Auth</h3>
  <div class="flex column center-vr gap-inherit height-100">
    <Button on:click={handleGithubLogin}>
      <GithubIcon />
      Login with GitHub
    </Button>
    <Button on:click={handleGitlabLogin} disabled>
      <GitlabIcon />
      Login with GitLab
    </Button>
    <Button on:click={handleBitbucketLogin} disabled>
      <ButbucketIcon/>
      Login with Bitbucket
    </Button>
  </div>
</main>
