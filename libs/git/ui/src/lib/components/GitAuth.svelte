<script lang="ts">
  import { env } from '@fp/infra/ui/data';
  import { Button } from '@fp/infra/components';
  import { GithubIcon, GitlabIcon } from '@lucide/svelte/icons';
  import ButbucketIcon from './icon/ButbucketIcon.svelte';

  const githubLogin = `${env.serverUrl}/git/login/github`;
  const gitlabLogin = `${env.serverUrl}/git/login/github`;
  const bitbucketLogin = `${env.serverUrl}/git/login/github`;

</script>

<style lang="scss">
  .container {
    margin-top: var(--fp-distance-4);
  }
</style>

<main class="height-100 center-text flex column gap-lg container">
  <h3>Login</h3>
  <div class="flex column center-vr gap-inherit height-100">
    <Button href={githubLogin}>
      <GithubIcon />
      Login with GitHub
    </Button>
    <Button  disabled>
      <GitlabIcon />
      Login with GitLab
    </Button>
    <Button href={bitbucketLogin} disabled>
      <ButbucketIcon/>
      Login with Bitbucket
    </Button>
  </div>
</main>
