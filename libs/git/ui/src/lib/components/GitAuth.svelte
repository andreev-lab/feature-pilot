<script lang="ts">
  import { env } from '@fp/infra/ui/data';
  import { Button } from '@fp/infra/components';

  function handleGithubLogin() {
    window.location.href = `${env.serverUrl}/git/login/github`;
  }
</script>

<div class="repo-list">
  <h3>Git Auth</h3>
  <Button on:click={handleGithubLogin}>
    Login with GitHub
  </Button>
</div>
