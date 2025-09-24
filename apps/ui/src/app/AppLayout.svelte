<script lang="ts">
  import { Layout, Sidebar, UserProfile } from '@fp/layout';
  import { GitRouting, GitService } from '@fp/git/ui';
  import { DropdownMenuTrigger, DropdownMenu, DropdownMenuContent, DropdownMenuItem } from '@fp/infra/components';
  import { Router } from 'svelte-routing';

  async function handleLogout() {
    await GitService.logout()
    window.location.reload();
  }
</script>

<Layout>
  <Router>
    <GitRouting/>
  </Router>
  {#snippet sidebar()}
    <Sidebar>
      {#snippet footer()}
        <DropdownMenu>
          <DropdownMenuTrigger>
            {#snippet child({props})}
              <button {...props}>
                <UserProfile />
              </button>
            {/snippet}
          </DropdownMenuTrigger>
          <DropdownMenuContent>
            <DropdownMenuItem onSelect={handleLogout}>Logout</DropdownMenuItem>
          </DropdownMenuContent>
        </DropdownMenu>
      {/snippet}
    </Sidebar>
  {/snippet}
</Layout>
